<template>
    <div class="p-4">
    <!-- barra de título -->
    <div class="flex justify-between items-center mb-4">
      <h1 class="text-2xl font-bold">Lista MSE</h1>

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
        <a href="#/about/cadastromse"className="btn btn-circle btn-sm">
          <svg xmlns="http://www.w3.org/2000/svg" className="w-8 h-8" fill="none" viewBox="0 0 24 24" strokeWidth="2.5" stroke="currentColor">
            <path strokeLinecap="round" strokeLinejoin="round" d="M12 4.5v15m7.5-7.5h-15" />
          </svg>
        </a>
      </div>
    </div>
    <div class="overflow-x-auto">
      <table class="table table-zebra w-full">
        <!-- Cabeçalho -->
        <thead>
          <tr>
            <th>ID</th>
            <th>Processo</th>
            <th>Adolescente</th>
            <th>Inicio</th>
            <th>Fim</th>
            <th>Tipo MSE</th>
            <th>Status</th>
          </tr>
        </thead>
        <!-- Corpo da Tabela -->
        <tbody>
          <tr v-for="(registro, id) in dados" :key="id"> <!--pra cada item de dados cria uma tabela usando registro como variavel e id como posição do item-->
            <td>{{ registro.id}}</td>
            <td>{{ registro.processo }}</td>
            <td>{{ registro.adolescente }}</td>
            <td>{{ registro.inicio}}</td>
            <td>{{ registro.fim}}</td>
            <td>{{ registro.tipo_mse}}</td>
            <td>{{ registro.concluida ? 'Concluído' : 'Vigente' }}</td>
            
            <!--modal de visualização-->
            <td>
              <button class="btn btn-sm btn-circle" @click="abrirModal(id)">
                <svg xmlns="http://www.w3.org/2000/svg" 
                    class="size-[1.2em]" 
                    fill="none" 
                    viewBox="0 0 24 24" 
                    stroke-width="2.5" 
                    stroke="currentColor">
                  <path stroke-linecap="round" 
                        stroke-linejoin="round" 
                        d="M2.25 12s3.75-6.75 9.75-6.75 
                          9.75 6.75 9.75 6.75-3.75 6.75-9.75 
                          6.75S2.25 12 2.25 12z" />
                  <path stroke-linecap="round" 
                        stroke-linejoin="round" 
                        d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                </svg>
              </button>
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
      <div class="modal-box">
        <form method="dialog">
          <button class="btn btn-sm btn-circle btn-ghost absolute right-2 top-2">X</button>
        </form>
        <h3 class="font-bold text-lg mb-2">Detalhes do Registro</h3>
        <p><strong>Nome:</strong> {{ registro.nome }}</p>
        <p><strong>Sexo:</strong> {{ registro.sexo }}</p>
        <p><strong>Início MSE:</strong> {{ registro.inicio_mse }}</p>
        <p><strong>Fim MSE:</strong> {{ registro.fim_mse }}</p>
        <p><strong>Ato Infracional:</strong> {{ registro.ato_infracional }}</p>
      </div>
    </dialog>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'  //acessa elementos e renderizar atualizando
import teste from './teste.json'  //importa os dados do json

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
