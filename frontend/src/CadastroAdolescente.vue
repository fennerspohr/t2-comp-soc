<template>
  <form class="form-cad-ad" @submit.prevent="submitForm">
    <fieldset class="fieldset bg-base-200 border-base-300 rounded-box w-xs border p-4">
      <legend class="fieldset-legend">Cadastro de Adolescente</legend>

      <label class="label">CPF</label>
      <input type="text" class="input" v-model="form.cpf" required />

      <label class="label">Nome</label>
      <input type="text" class="input" v-model="form.nome" required />

      <label class="label">Nome Social</label>
      <input type="text" class="input" v-model="form.nomeSocial" required />

      <label class="label">Sexo</label>
      <select class="select" v-model="form.sexo" required>
        <option disabled value="">Selecione</option>
        <option>Feminino</option>
        <option>Masculino</option>
        <option>Outro</option>
      </select>

      <label class="label">Endereço</label>
      <input type="text" class="input" v-model="form.endereco" required />

      <label class="label">Bairro</label>
      <input type="text" class="input" v-model="form.bairro" required />

      <label class="label">Data de Nascimento</label>
      <input type="date" class="input" v-model="form.dataNascimento" required />

      <label class="label">Tem CT?</label>
      <input
        type="checkbox"
        class="checkbox"
        v-model="form.temCT"
      />

      <label class="label">Nome CT</label>
      <input
        type="text"
        class="input"
        v-model="form.nomeCT"
        :disabled="!form.temCT"
        :required="form.temCT"
      />
      <div>
      <button class="btn">Cadastrar</button>
    </div>
    </fieldset>
    
  </form>
</template>

<script setup>
import { computed, reactive, watch } from 'vue'

// Estado reativo do formulário
const form = reactive({
  cpf: '',
  nome: '',
  nomeSocial: '',
  sexo: '',
  endereco: '',
  bairro: '',
  dataNascimento: '',
  temCT: false,
  nomeCT: ''
})

// funcao para cuidar do tem ct - se nao estiver marcado nao deixa preencher o nome e se desmarcar com ele preenchido apaga o nome
watch(() => form.temCT, (checked) => {
  if (!checked) {
    form.nomeCT = ''
  }
})

function submitForm() {
  console.log('Dados enviados:', form) //apenas printa os dados que ele pegou do form no console
}

</script>

<style>
.form-cad-ad {
  display: flex;
  justify-content: center;
}
</style>
