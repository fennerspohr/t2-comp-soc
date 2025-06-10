<template>
  <form class="form-cad-ad" @submit.prevent="salvar">
    <fieldset class="fieldset bg-base-200 border-base-300 rounded-box w-xs border p-4">
      <legend class="fieldset-legend">Editar MSE</legend>

      <label class="label mt-2">Número do Processo</label>
      <input type="text" class="input" v-model="form.processo_num" required maxlength="13" />

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

      <label class="label mt-2">Data de Início</label>
      <input type="date" class="input" v-model="form.data_inicio" required />

      <label class="label mt-2">Data de Finalização</label>
      <input type="date" class="input" v-model="form.data_fim" required />

      <label class="label mt-2">Status da MSE</label>
      <select v-model="form.concluida" required>
        <option disabled value="">Selecione</option>
        <option :value="true">Finalizada</option>
        <option :value="false">Vigente</option>
      </select>

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

      <div v-if="form.tipo_finalizacao === 1">
        <label class="label mt-2">Motivo da Interrupção</label>
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

      <label class="label mt-2">Caixa Baixa</label>
      <input type="text" class="input" v-model="form.caixa_baixa_num" required />

      <div class="mt-4">
        <button class="btn" type="submit">Salvar Alterações</button>
      </div>
    </fieldset>
  </form>
</template>

<script setup>
import { ref, reactive, onMounted, computed, watch } from 'vue'
import axios from 'axios'

// Pega o ID da URL
const id = window.location.hash.split('/').pop()

// Listas
const infracoes = ref([])
const adolescentes = ref([])
const orientadores = ref([])

// Estado do form
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

// Carrega listas e MSE
onMounted(async () => {
  try {
    const [infRes, adoRes, oriRes, mseRes] = await Promise.all([
      axios.get('http://127.0.0.1:8000/api/atoinfracional/'),
      axios.get('http://127.0.0.1:8000/api/adolescente/'),
      axios.get('http://127.0.0.1:8000/api/orientadores'),
      axios.get(`http://127.0.0.1:8000/api/mse/?id=${id}`)
    ])
    infracoes.value = infRes.data
    adolescentes.value = adoRes.data
    orientadores.value = oriRes.data
    const mse = mseRes.data

    // Preenche o form
    Object.assign(form, {
      id: mse.id,
      processo_num: mse.processo_num,
      infracao: mse.infracao.id,
      tipo_mse: mse.tipo_mse,
      id_adolescente: mse.id_adolescente.id,
      id_orientador: mse.id_orientador.id,
      data_inicio: mse.data_inicio,
      data_fim: mse.data_fim,
      tipo_finalizacao: mse.tipo_finalizacao,
      tipo_interrupcao: mse.tipo_interrupcao,
      caixa_baixa_num: mse.caixa_baixa_num,
      concluida: mse.concluida
    })
  } catch (error) {
    console.error('Erro ao carregar dados:', error)
  }
})

// Watchers
watch(() => form.concluida, (newVal) => {
  if (newVal !== true) {
    form.tipo_finalizacao = ''
    form.tipo_interrupcao = ''
  }
})

watch(() => form.tipo_finalizacao, (newVal) => {
  if (newVal !== 1) {
    form.tipo_interrupcao = ''
  }
})

// Validações
const verifica = computed(() => {
  return (
    form.processo_num &&
    form.infracao &&
    form.id_adolescente &&
    form.tipo_mse !== '' &&
    form.id_orientador &&
    form.data_inicio &&
    form.data_fim &&
    form.caixa_baixa_num &&
    form.concluida !== '' &&
    (form.concluida !== true || form.tipo_finalizacao !== null) &&
    (form.tipo_finalizacao !== 1 || form.tipo_interrupcao !== null) &&
    new Date(form.data_fim) >= new Date(form.data_inicio)
  )
})

// Envia os dados atualizados
function salvar() {
  const payload = {
    ...form,
    tipo_mse: Number(form.tipo_mse),
    tipo_finalizacao: form.tipo_finalizacao !== '' ? Number(form.tipo_finalizacao) : null,
    tipo_interrupcao: form.tipo_interrupcao !== '' ? Number(form.tipo_interrupcao) : null
  }

  axios.post('http://127.0.0.1:8000/api/mse/update', payload)
    .then(response => {
      console.log('MSE atualizada:', response.data)
      alert('Medida atualizada com sucesso!')
    })
    .catch(error => {
      console.error('Erro ao atualizar MSE:', error)
      alert('Erro ao atualizar a medida.')
    })
}
</script>

<style>
.form-cad-ad {
  display: flex;
  justify-content: center;
}
</style>
