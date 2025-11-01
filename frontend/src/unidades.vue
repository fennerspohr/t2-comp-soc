<template>
  <div class="p-8 flex flex-col items-center min-h-screen bg-base-100">
    <!-- Barra de título e filtros -->
    <div class="w-full flex justify-end mb-6">
      <!-- barra de pesquisa -->
      <div class="flex items-center gap-2">
        <label class="input input-bordered input-primary w-64 h-9 flex items-center gap-2">
          <svg class="h-[1em] opacity-50" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
            <g stroke-linejoin="round" stroke-linecap="round" stroke-width="2.5" fill="none" stroke="currentColor">
              <circle cx="11" cy="11" r="8"></circle>
              <path d="m21 21-4.3-4.3"></path>
            </g>
          </svg>
          <input 
            v-model="campoBusca" 
            type="search" 
            placeholder="Buscar unidade" 
            class="w-full outline-none"
          />
        </label>

        <button class="btn btn-sm btn-primary h-9" @click="aplicarBusca">
          Buscar
        </button>

        <button class="btn btn-outline btn-error btn-sm h-9" @click="limparFiltros">
          Limpar
        </button>
      </div>
    </div>

    <!-- Tabela centralizada -->
    <div class="w-full flex justify-center">
      <div class="overflow-x-auto w-2/3">
        <table class="table table-zebra w-full text-center shadow-md rounded-lg">
          <!-- Cabeçalho -->
          <thead>
            <tr>
              <th class="text-lg">Unidades</th>
            </tr>
          </thead>
          <!-- Corpo -->
          <tbody>
            <tr v-for="(registro, id) in dadosFiltrados" :key="id">
              <td>
                <router-link 
                  :to="`/tela/${id}`" 
                  class="text-blue-600 hover:underline"
                >
                  {{ registro.nome }}
                </router-link>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import axios from 'axios'

const dados = ref([])         // Armazena as unidades
const filtro = ref('')
const campoBusca = ref('')

// Buscar unidades quando o componente montar
onMounted(async () => {
  try {
    const response = await axios.get('http://172.27.3.101:5000/unidades')
    dados.value = response.data   // Armazena os dados na variável
  } catch (error) {
    console.error('Erro ao buscar unidades:', error)
  }
})

// Computed para filtrar resultados pelo campo de busca
const dadosFiltrados = computed(() => {
  return dados.value.filter(registro => {
    const textoBusca = filtro.value.toLowerCase()
    return registro.nome?.toLowerCase().includes(textoBusca)
  })
})

// Funções de busca
function aplicarBusca() {
  filtro.value = campoBusca.value.trim()
}

function limparFiltros() {
  campoBusca.value = ''
  filtro.value = ''
}
</script>
