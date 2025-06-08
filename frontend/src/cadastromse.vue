<template>
  <form class="form-cad-ad" @submit.prevent="submitForm">
    <fieldset class="fieldset bg-base-200 border-base-300 rounded-box w-xs border p-4">
      <legend class="fieldset-legend">Cadastro de MSE</legend>

      <label class="label mt-2">Número do Processo</label>
      <input type="text" class="input" v-model="form.processo_num" required maxlength=13 />

      <label class="label mt-2">Ato Infracional</label>
      <select class="select" v-model="form.infracao" required>
        <option disabled value="">Selecione</option>
        <option v-for="infracao in infracoes" :key="infracao.id" :value="infracao.id">
          {{ infracao.nome }}
        </option>
      </select>

      <label class="label mt-2">Adolescente</label>
      <select class="select" v-model="form.id_adolescente" required>
        <option disabled value="">Selecione</option>
        <option v-for="adolescente in adolescentes" :key="adolescente.id" :value="adolescente.id">
          {{ adolescente.nome }}
        </option>
      </select>

      <label class="label mt-2">Tipo MSE</label>
      <select class="select" v-model.number="form.tipo_mse" required>
        <option disabled value="">Selecione</option>
        <option value="0">LA</option>
        <option value="1">PSC</option>
        <option value="2">LA com PSC</option>
      </select>

      <label class="label mt-2">Orientador</label>
      <select class="select" v-model="form.id_orientador" required>
        <option disabled value="">Selecione</option>
        <option v-for="orientador in orientadores" :key="orientador.id" :value="orientador.id">
          {{ orientador.nome }}
        </option>
      </select>


      <label class="label mt-2">Data de Inicio</label>
      <input type="date" class="input" v-model="form.data_inicio" required />

      <label class="label mt-2">Data de Finalização</label>
      <input type="date" class="input" v-model="form.data_fim" required />

      <!-- status da mse -->
      <label class="label mt-2">Status da MSE</label>
      <select v-model="form.concluida" required>
        <option disabled value="">Selecione</option>
        <option :value="true">Finalizada</option>
        <option :value="false">Vigente</option>
      </select>


      <!-- se tiver finalizada, mostra tipo de finalização -->
      <div v-if="form.concluida === true">
        <label class="label mt-2">Tipo de Finalização</label>
        <select v-model.number="form.tipo_finalizacao" required>
          <option disabled value="">Selecione</option>
          <option value="0">Concluída</option>
          <option value="1">Interrompida</option>
          <option value="2">Transferida</option>
          <option value="3">Regredida</option>
        </select>
      </div>

      <!-- se for interrompida, mostra motivo da interrupção -->
      <div v-if="form.tipo_finalizacao === 1">
        <label class=" label mt-2">Motivo da Interrupção</label>
        <select v-model.number="form.tipo_interrupcao" required>
          <option disabled value="">Selecione</option>
          <option value="0">Case</option>
          <option value="1">PRSM ou outra penitenciária</option>
          <option value="2">Desistência</option>
          <option value="3">Extinta pelo Judiciário (prescrição)</option>
          <option value="4">Idade</option>
          <option value="5">Revogada (não cumpre)</option>
        </select>
      </div>
      <div>
        <label class="label mt-2">Caixa Baixa</label>
        <input type="text" class="input" v-model="form.caixa_baixa_num" required />

        <!-- botão que só funciona se tudo estiver preenchido -->
        <button class="btn" :disabled="!verifica" @click="salvar()">Cadastrar</button>
      </div>
    </fieldset>

  </form>
  {{ form }}
</template>

<script setup>

import { computed, reactive, watch, ref, onMounted } from 'vue'
import axios from 'axios'

const infracoes = ref([])
const adolescentes = ref([])
const orientadores = ref([])

onMounted(async () => {
  try {
    const response = await axios.get('http://127.0.0.1:8000/api/atoinfracional/')
    infracoes.value = response.data
    console.log('Infrações carregadas:', infracoes.value)
  } catch (error) {
    console.error('Erro ao carregar infrações:', error)
  }

  try {
    const response = await axios.get('http://127.0.0.1:8000/api/adolescente/')
    adolescentes.value = response.data
    console.log('Adolescentes:', adolescentes.value)
  } catch (error) {
    console.error('Erro ao carregar o registro:', error)
  }

  try {
    const response = await axios.get('http://127.0.0.1:8000/api/orientadores')
    orientadores.value = response.data
    console.log('Adolescentes:', orientadores.value)
  } catch (error) {
    console.error('Erro ao carregar o registro:', error)
  }

})

// Estado reativo do formulário
const form = reactive({
  id: '',
  processo_num: '',
  infracao: '',
  tipo_mse: '',
  id_adolescente: '',
  id_orientador: '',
  data_inicio: '',
  data_fim: '',
  tipo_finalizacao: null,
  tipo_interrupcao: null,
  caixa_baixa_num: '',
  concluida: ''
})

//pra preencher depois quando for usar
const tipoMSELabel = {
  0: 'Liberdade Assistida',
  1: 'Prestação de Serviços à Comunidade',
  2: 'LA com PSC'
}

console.log('Tipo MSE:', tipoMSELabel[form.tipo_mse])

const tipofinalizacaochoice = {
  0: 'Concluída',
  1: 'Interrompida',
  2: 'Transferida',
  3: 'Regredida'
}

console.log('Finalização:', tipofinalizacaochoice[form.tipo_finalizacao])

const tipointerrupcaochoice = {
  0: 'Case',
  1: 'PRSM ou outra penitenciária',
  2: 'Desistência',
  3: 'Extinta pelo Judiciário (prescrição)',
  4: 'Idade',
  5: 'Revogada (não cuumpre)'
}

console.log('Interrupção:', tipointerrupcaochoice[form.tipo_interrupcao])

// aqui eu verifico se todos os campos obrigatórios estão preenchidos
const formIsValid = computed(() => {
  return (
    form.processo_num &&
    form.infracao &&
    form.id_adolescente &&
    form.tipo_mse &&
    form.id_orientador &&
    form.data_inicio &&
    form.data_fim &&
    form.caixa_baixa_num &&
    form.concluida !== '' &&

    // se tiver finalizada, obrigar escolher tipo de finalização
    (form.concluida !== true || form.tipo_finalizacao) &&

    // se for interrompida, obrigar escolher motivo
    (form.tipo_finalizacao !== 'interrompida' || form.tipo_interrupcao)
  )
})

watch(() => form.concluida, (newVal) => {
  if (newVal !== true) {
    form.tipo_finalizacao = ''
    form.tipo_interrupcao = ''
  }
})

//correção de erro que ao clicar em interrompida e depois sair disso continuava aparecendo o campo
watch(() => form.tipo_finalizacao, (newVal) => {
  if (newVal !== '1') {
    form.tipo_interrupcao = ''
  }
})

//garantia de que o fim não pode seja anterior ao inicio
const dataValida = computed(() => {
  return new Date(form.data_fim) >= new Date(form.data_inicio)
})

const verifica = computed(() => formIsValid.value && dataValida.value)

function salvar() {

  form.tipo_mse = form.tipo_mse === '' ? null : Number(form.tipo_mse)
  form.tipo_finalizacao = form.tipo_finalizacao === '' ? null : Number(form.tipo_finalizacao)
  form.tipo_interrupcao = form.tipo_interrupcao === '' ? null : Number(form.tipo_interrupcao)

  const apiUrl = 'http://127.0.0.1:8000/api/mse/';

  axios.post(apiUrl, form)
    .then((response) => {
      console.log(response.data)
      alert('Medida cadastrada com sucesso!')
    })
    .catch((error) => {
      console.error('Erro ao cadastrar:', error)
      alert('Erro ao cadastrar medida. Verifique os dados.')
    })
}

</script>

<style>
.form-cad-ad {
  display: flex;
  justify-content: center;
}
</style>