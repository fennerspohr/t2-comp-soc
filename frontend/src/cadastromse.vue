<template>
  <form class="form-cad-ad" @submit.prevent="submitForm">
    <fieldset class="fieldset bg-base-200 border-base-300 rounded-box w-xs border p-4">
      <legend class="fieldset-legend">Cadastro de MSE</legend>

      <label class="label mt-2">Número do Processo</label>
      <input type="text" class="input" v-model="form.processo_num" required />

      <label class="label mt-2">Ato Infracional</label>
      <input type="text" class="input" v-model="form.ato_infracional" required />

      <label class="label mt-2">ID Adolescente</label>
      <input type="text" class="input" v-model="form.idAdolescente" required />

      <label class="label mt-2">Tipo MSE</label>
      <select class="select" v-model.number="form.tipo_MSE" required>
        <option disabled value="">Selecione</option>
        <option value="0">LA</option>
        <option value="1">PSC</option>
        <option value="2">LA com PSC</option>
      </select>

      <label class="label mt-2">ID Orientador</label>
      <input type="text" class="input" v-model="form.idOrientador" required />

      <label class="label mt-2">Data de Inicio</label>
      <input type="date" class="input" v-model="form.data_inicio" required />

      <label class="label mt-2">Data de Finalização</label>
      <input type="date" class="input" v-model="form.data_fim" required />

        <!-- status da mse -->
        <label class="label mt-2">Status da MSE</label>
        <select v-model="form.status" required>
        <option disabled value="">Selecione</option>
        <option :value="true">Finalizada</option>
        <option :value="false">Vigente</option>
        </select>


         <!-- se tiver finalizada, mostra tipo de finalização -->
        <div v-if="form.status === true">
            <label class="label mt-2">Tipo de Finalização</label>
            <select v-model="form.tipo_finalizacao" required>
                <option disabled value="">Selecione</option>
                <option value="finalizada">Finalizada (Cumpriu os objetivos)</option>
                <option value="interrompida">Interrompida (Extinta pelo juiz)</option>
                <option value="transferida">Transferida (Deprecada)</option>
                <option value="regredida">Regredida (Não cumpriu, regrediu)</option>
            </select>
            </div>

        <!-- se for interrompida, mostra motivo da interrupção -->
        <div v-if="form.tipo_finalizacao === 'interrompida'">
        <label class=" label mt-2">Motivo da Interrupção</label>
        <select v-model="form.tipo_interrupcao" required>
            <option disabled value="">Selecione</option>
            <option value="prisao">CASE, PRSM ou penitenciária</option>
            <option value="desistencia">Desistência</option>
            <option value="prescricao">Prescrição</option>
            <option value="idade">Idade</option>
            <option value="revogada">Revogada por descumprimento</option>
        </select>
        </div>
      <div>
    <label class="label mt-2">Caixa Baixa</label>
    <input type="text" class="input" v-model="form.num_caixa_baixa" required />

     <!-- botão que só funciona se tudo estiver preenchido -->
      <button class="btn" :disabled="!dataValida">Cadastrar</button>
    </div>
    </fieldset>
    
  </form>
</template>

<script setup>
import { computed, reactive, watch } from 'vue'

// Estado reativo do formulário
const form = reactive({
  id: '',
  processo_num: '',
  ato_infracional: '',
  tipo_MSE: '',
  idAdolescente: '',
  idOrientador: '',
  data_inicio: '',
  data_fim: '',
  tipo_finalizacao: '',
  tipo_interrupcao: '',
  num_caixa_baixa:''
})

//pra preencher depois quando for usar
const tipoMSELabel = {
  0: 'LA',
  1: 'PSC',
  2: 'LA com PSC'
}

console.log('Tipo MSE:', tipoMSELabel[form.tipo_MSE])

//mensagem de sucesso ao enviar
function submitForm() {
  console.log('Dados enviados:', JSON.parse(JSON.stringify(form)))
  alert('Medida cadastrada com sucesso!')
}

// aqui eu verifico se todos os campos obrigatórios estão preenchidos
const formIsValid = computed(() => {
  return (
    form.processo_num &&
    form.ato_infracional &&
    form.idAdolescente &&
    form.tipo_MSE &&
    form.idOrientador &&
    form.data_inicio &&
    form.data_fim &&
    form.num_caixa_baixa &&
    form.status !== '' &&

    // se tiver finalizada, obrigar escolher tipo de finalização
    (form.status !== true || form.tipo_finalizacao) &&

    // se for interrompida, obrigar escolher motivo
    (form.tipo_finalizacao !== 'interrompida' || form.tipo_interrupcao)
  )
})

watch(() => form.status, (newVal) => {
  if (newVal !== true) {
    form.tipo_finalizacao = ''
    form.tipo_interrupcao = ''
  }
})

//correção de erro que ao clicar em interrompida e depois sair disso continuava aparecendo o campo
watch(() => form.tipo_finalizacao, (newVal) => {
  if (newVal !== 'interrompida') {
    form.tipo_interrupcao = ''
  }
})

//garantia de que o fim não pode seja anterior ao inicio
const dataValida = computed(() => {
  return new Date(form.data_fim) >= new Date(form.data_inicio)
})



</script>

<style>
.form-cad-ad {
  display: flex;
  justify-content: center;
}
</style>
