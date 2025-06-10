<template>
  <form class="form-cad-ad" @submit.prevent="salvar">
    <fieldset class="fieldset bg-base-200 border-base-300 rounded-box w-xs border p-4">
      <legend class="fieldset-legend">Atualização de Adolescente</legend>

      <label class="label mt-2">CPF</label>
      <input type="text" class="input" v-model="form.cpf" required maxlength="11"/>

      <label class="label mt-2">Nome</label>
      <input type="text" class="input" v-model="form.nome" required maxlength=100/>

      <label class="label mt-2">Nome Social</label>
      <input type="text" class="input" v-model="form.nome_social" maxlength=100/>

      <label class="label mt-2">Sexo</label>
      <select class="select" v-model.number="form.sexo" required>
        <option disabled value="">Selecione</option>
        <option value="0">Masculino</option>
        <option value="1">Feminino</option>
        <option value="2">Outro</option>
      </select>

      <label class="label mt-2">Endereço</label>
      <input type="text" class="input" v-model="form.endereco" required maxlength=255/>

      <label class="label mt-2">Bairro</label>
      <input type="text" class="input" v-model="form.bairro" required maxlength=100/>

      <label class="label">Data de Nascimento</label>
      <input type="date" class="input" v-model="form.data_nasc" required />

      <label class="label mt-2">Nome da Mãe</label>
      <input type="text" class="input" v-model="form.nome_mae" maxlength=100/>

      <label class="label mt-2">Tem CT?</label>
      <input
        type="checkbox"
        class="checkbox"
        v-model="form.tem_CT"
      />

      <label class="label mt-2">Nome CT</label>
      <input
        type="text"
        class="input"
        v-model="form.nome_CT"
        :disabled="!form.tem_CT"
        :required="form.tem_CT"
        maxlength=100
      />

      <label class="label mt-2">Contatos</label>
      <div class="flex gap-2 mb-2">
        <input
          type="text"
          class="input flex-1"
          v-model="novoContato"
          placeholder="Digite um novo contato"
          maxlength=13
        />
        <button
          type="button"
          class="btn btn-primary"
          @click="adicionarContato"
          :disabled="!novoContato.trim()"
        >
          +
        </button>
      </div>

      <ul class="list-disc pl-5 mb-2">
        <li v-for="(contato, index) in form.contatos" :key="index" class="flex justify-between items-center">
          {{ contato.telefone? contato.telefone : contato }}
          <button type="button" class="btn btn-xs btn-error" @click="removerContato(index)">Remover</button>
        </li>
      </ul>
      <div>
      <button class="btn" type="submit">Salvar Alterações</button>
    </div>
    </fieldset>
    
  </form>

</template>

<script setup>
import { ref, reactive, watch, onMounted } from 'vue'
import axios from 'axios'

//pegando id da URL manualmente
const currentPath = window.location.hash
const id = currentPath.split('/').pop()

// Estado reativo do formulário
const form = reactive({
  id: '',
  cpf: '',
  nome: '',
  nome_social: '',
  sexo: '',
  endereco: '',
  bairro: '',
  data_nasc: '',
  nome_mae: '',
  tem_CT: false,
  nome_CT: '',
  contatos: []
})

//busca os dados
onMounted(() => {
  // pega os dados de todos os adolescentes

  const apiUrl = 'http://127.0.0.1:8000/api/adolescente/'

  axios.get(`${apiUrl}?id=${id}`)
    .then((response) => {
      const data = response.data
      form.id = data.id
      form.cpf = data.cpf
      form.nome = data.nome
      form.nome_social = data.nome_social
      form.sexo = data.sexo
      form.endereco = data.endereco
      form.bairro = data.bairro
      form.data_nasc = data.data_nasc
      form.nome_mae = data.nome_mae
      form.tem_CT = data.tem_CT
      form.nome_CT = data.nome_CT
      form.contatos = data.contatos || [] 
    })
    .catch((error) => {
      console.error('Error fetching data:', error)
    });
})

// funcao para cuidar do tem ct - se nao estiver marcado nao deixa preencher o nome e se desmarcar com ele preenchido apaga o nome
watch(() => form.tem_CT, (checked) => {
  if (!checked) {
    form.nome_CT = ''
  }
})

const sexoAdolescente = {
  0: 'Masculino',
  1: 'Feminino',
  2: 'Outro'
}

function submitForm() {
  console.log('Dados enviados:', JSON.parse(JSON.stringify(form))) //apenas printa os dados que ele pegou do form no console
  alert('Adolescente atualizado com sucesso!')
}

const novoContato = ref('')

function adicionarContato() {
  if (novoContato.value.trim()) {
    form.contatos.push(novoContato.value.trim())
    novoContato.value = ''
  }
}

function removerContato(index) {
  form.contatos.splice(index, 1)
}


function salvar() {
  const apiUrlUpd = 'http://127.0.0.1:8000/api/adolescente/update'

  axios.post(apiUrlUpd, {
    form  
  })
    .then((response) => {
      console.log('Atualização bem-sucedida:', response.data)
      alert('Adolescente atualizado com sucesso!')
    })
    .catch((error) => {
      console.error('Erro ao atualizar adolescente:', error)
    })
}

</script>

<style>
.form-cad-ad {
  display: flex;
  justify-content: center;
}
</style>
