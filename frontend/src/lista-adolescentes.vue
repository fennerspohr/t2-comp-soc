<template>
    <div class="p-4">
    <!-- barra de título -->
    <div class="flex justify-between items-center mb-4">
      <h1 class="text-2xl font-bold">Adolescentes</h1>

      <div class="flex gap-2">
        <!-- barra de pesquisa-->
        <label class="input">
          <svg class="h-[1em] opacity-50" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
            <g
              stroke-linejoin="round"
              stroke-linecap="round"
              stroke-width="2.5"
              fill="none"
              stroke="currentColor"
            >
              <circle cx="11" cy="11" r="8"></circle>
              <path d="m21 21-4.3-4.3"></path>
            </g>
          </svg>
          <input type="search" required placeholder="Pesquisar" />
        </label>
        <!--botão de adicionar-->
        <a href="#/about/cadastro-adolescente" class="btn btn-soft btn-primary">
          <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" viewBox="0 0 448 512" fill="currentColor">
            <path d="M256 80c0-17.7-14.3-32-32-32s-32 14.3-32 32l0 144L48 224c-17.7 0-32 14.3-32 32s14.3 32 32 32l144 0 0 144c0 17.7 14.3 32 32 32s32-14.3 32-32l0-144 144 0c17.7 0 32-14.3 32-32s-14.3-32-32-32l-144 0 0-144z"/>
          </svg>
        </a>
      </div>
    </div>
    <div class="overflow-x-auto">
      <table class="table table-zebra w-full">
        <!-- Cabeçalho -->
        <thead>
          <tr>
            <th>CPF</th>
            <th>Nome</th>
            <th>Sexo</th>
            <th>Data de Nascimento</th>
            <th>CT</th>
          </tr>
        </thead>
        <!-- Corpo da Tabela -->
        <tbody>
          <tr v-for="(registro, id) in dados" :key="id"> <!--pra cada item de dados cria uma tabela usando registro como variavel e id como posição do item-->
            <td>{{ registro.cpf}}</td>
            <td>{{ registro.nome }}</td>
            <td>{{ registro.sexo == 0 ? 'Masculino' : registro.sexo == 1 ? 'Feminino' : 'Outro' }}</td> 
            <td>{{ registro.data_nasc }}</td>
            <td>{{ registro.tem_ct ? registro.nome_ct : 'Não possui' }}</td>
            
            <!--modal de visualização-->
            <td>
          <button class="btn btn-soft btn-primary" @click="abrirModal(id)">
            <svg xmlns="http://www.w3.org/2000/svg" 
                class="w-5 h-5" 
                viewBox="0 0 576 512" 
                fill="currentColor">
              <path d="M288 32c-80.8 0-145.5 36.8-192.6 80.6C48.6 156 17.3 208 2.5 243.7c-3.3 7.9-3.3 16.7 0 24.6C17.3 304 48.6 356 95.4 399.4C142.5 443.2 207.2 480 288 480s145.5-36.8 192.6-80.6c46.8-43.5 78.1-95.4 93-131.1c3.3-7.9 3.3-16.7 0-24.6c-14.9-35.7-46.2-87.7-93-131.1C433.5 68.8 368.8 32 288 32zM144 256a144 144 0 1 1 288 0 144 144 0 1 1 -288 0zm144-64c0 35.3-28.7 64-64 64c-7.1 0-13.9-1.2-20.3-3.3c-5.5-1.8-11.9 1.6-11.7 7.4c.3 6.9 1.3 13.8 3.2 20.7c13.7 51.2 66.4 81.6 117.6 67.9s81.6-66.4 67.9-117.6c-11.1-41.5-47.8-69.4-88.6-71.1c-5.8-.2-9.2 6.1-7.4 11.7c2.1 6.4 3.3 13.2 3.3 20.3z"/>
            </svg>
          </button>


            </td>

            <!--botão de editar-->
            <td>
          <a :href="`#/editar-adolescente/${registro.id}`" class="btn btn-soft btn-primary">
            <svg xmlns="http://www.w3.org/2000/svg" 
                class="w-5 h-5" 
                viewBox="0 0 512 512" 
                fill="currentColor">
              <path d="M471.6 21.7c-21.9-21.9-57.3-21.9-79.2 0L362.3 51.7l97.9 97.9 30.1-30.1c21.9-21.9 21.9-57.3 0-79.2L471.6 21.7zm-299.2 220c-6.1 6.1-10.8 13.6-13.5 21.9l-29.6 88.8c-2.9 8.6-.6 18.1 5.8 24.6s15.9 8.7 24.6 5.8l88.8-29.6c8.2-2.7 15.7-7.4 21.9-13.5L437.7 172.3 339.7 74.3 172.4 241.7zM96 64C43 64 0 107 0 160L0 416c0 53 43 96 96 96l256 0c53 0 96-43 96-96l0-96c0-17.7-14.3-32-32-32s-32 14.3-32 32l0 96c0 17.7-14.3 32-32 32L96 448c-17.7 0-32-14.3-32-32l0-256c0-17.7 14.3-32 32-32l96 0c17.7 0 32-14.3 32-32s-14.3-32-32-32L96 64z"/>
            </svg>
          </a>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <!-- modal para cada item -->
    <dialog
      v-for="(registro, id) in dados" 
      :id="`modal-${id}`"
      :key="`modal-${id}`"
      class="modal"
    >
      <div class="modal-box text-left">
        <form method="dialog">
          <button class="btn btn-sm btn-circle btn-ghost absolute right-2 top-2">X</button>
        </form>
        <h3 class="font-bold text-lg mb-2">Detalhes do Registro</h3>
        <p><strong>Id:</strong> {{ registro.id }}</p>
        <p><strong>CPF:</strong> {{ registro.cpf }}</p>
        <p><strong>Nome:</strong> {{ registro.nome }}</p>
        <p><strong>Nome Social:</strong> {{ registro.nome_social }}</p>
        <p><strong>Sexo:</strong> {{ registro.sexo == 0 ? 'Masculino' : registro.sexo == 1 ? 'Feminino' : 'Outro' }}</p>
        <p><strong>Data de Nascimento:</strong> {{ registro.data_nasc }}</p>
        <p><strong>Endereço:</strong> {{ registro.endereco }}</p>
        <p><strong>Bairro:</strong> {{ registro.bairro }}</p>
        <p><strong>Nome da Mãe:</strong> {{ registro.nome_mae }}</p>
  
      </div>
    </dialog>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'  //acessa elementos e renderizar atualizando
import teste from './teste-adolescente.json'  //importa os dados do json

const dados = ref([]) //cria uma lista vazia
const filtro = ref('') //filtro da busca

onMounted(() => {
  dados.value = teste //ao carregar a pagina preenche os dados com o JSON
})

//abre a visualização 
function abrirModal(id) {
  document.getElementById(`modal-${id}`).showModal()
}
</script>

<style scoped>
</style>