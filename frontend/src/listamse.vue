<template>
  <div class="p-4">
    <!-- barra de título -->
    <div class="flex justify-between items-center mb-4">
      <h1 class="text-2xl font-bold">Lista MSE</h1>


      <!--filtros-->
      <div class="flex flex-col gap-2 mr-10">


        <!-- barra de pesquisa -->
        <div class="flex items-center gap-2">
          <label class="input input-bordered input-primary w-64 h-8 flex items-center gap-2">
            <svg class="h-[1em] opacity-50" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
              <g stroke-linejoin="round" stroke-linecap="round" stroke-width="2.5" fill="none" stroke="currentColor">
                <circle cx="11" cy="11" r="8"></circle>
                <path d="m21 21-4.3-4.3"></path>
              </g>
            </svg>
            <input v-model="campoBusca" type="search" placeholder="Número do processo ou nome" />
          </label>
          <button class="btn btn-sm btn-primary h-8" @click="aplicarBusca">
            Buscar
          </button>
        </div>




        <!-- linha com select + status -->
        <div class="flex items-center gap-2">
          <!-- filtro ano -->
          <select class="select select-primary w-24 h-8 text-sm" v-model="anoSelecionado">
            <option disabled value="">Ano</option>
            <option v-for="ano in anosDisponiveis" :key="ano" :value="ano.toString()">
              {{ ano }}
            </option>
          </select>


          <!-- filtro de status -->
          <!-- filtro de status (como select) -->
          <select class="select select-primary w-29 h-8 text-sm" v-model="statusSelecionado">
            <option disabled value="">Status</option>
            <option value="vigente">Vigente</option>
            <option value="finalizada">Finalizada</option>
          </select>


          <!-- botão de limpar filtros -->
          <button class="btn btn-outline btn-error btn-sm h-8" @click="limparFiltros">
            Limpar filtros
          </button>
        </div>
      </div>
    </div>


    <div class="overflow-x-auto">
      <table class="table table-zebra w-full">
        <!-- Cabeçalho -->
        <thead>
          <tr>
            <th>Processo</th>
            <th>Ato Infracional</th>
            <th>Tipo MSE</th>
            <th>Adolescente</th>
            <th>Orientador</th>
            <th>Inicio</th>
            <th>Fim</th>
            <th>Situação</th>
          </tr>
        </thead>
        <!-- Corpo da Tabela -->
        <tbody>
          <tr v-for="(registro, id) in dadosFiltrados" :key="id">
            <!--pra cada item de dados cria uma tabela usando registro como variavel e id como posição do item-->
            <td>{{ registro.processo_num }}</td>
            <td>{{ registro.infracao.nome }}</td>
            <td>{{ formatarTipoMse(registro.tipo_mse) }}</td>
            <td>{{ registro.id_adolescente.nome }}</td>
            <td>{{ registro.id_orientador.nome }}</td>
            <td>{{ registro.data_inicio }}</td>
            <td>{{ registro.data_fim }}</td>
            <td>
              <span :class="registro.concluida ? 'text-red-500 font-semibold' : 'text-green-600 font-semibold'">
                {{ registro.concluida ? 'Finalizada' : 'Vigente' }}
              </span>
            </td>



            <!--modal de visualização-->
            <td>
              <button class="btn btn-soft btn-primary mr-2" @click="abrirModal(id)">
                <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" viewBox="0 0 576 512" fill="currentColor">
                  <path
                    d="M288 32c-80.8 0-145.5 36.8-192.6 80.6C48.6 156 17.3 208 2.5 243.7c-3.3 7.9-3.3 16.7 0 24.6C17.3 304 48.6 356 95.4 399.4C142.5 443.2 207.2 480 288 480s145.5-36.8 192.6-80.6c46.8-43.5 78.1-95.4 93-131.1c3.3-7.9 3.3-16.7 0-24.6c-14.9-35.7-46.2-87.7-93-131.1C433.5 68.8 368.8 32 288 32zM144 256a144 144 0 1 1 288 0 144 144 0 1 1 -288 0zm144-64c0 35.3-28.7 64-64 64c-7.1 0-13.9-1.2-20.3-3.3c-5.5-1.8-11.9 1.6-11.7 7.4c.3 6.9 1.3 13.8 3.2 20.7c13.7 51.2 66.4 81.6 117.6 67.9s81.6-66.4 67.9-117.6c-11.1-41.5-47.8-69.4-88.6-71.1c-5.8-.2-9.2 6.1-7.4 11.7c2.1 6.4 3.3 13.2 3.3 20.3z" />
                </svg>
              </button>


              <!--botão de editar-->
              <!--coloca o registro.id em js p abrir cada um-->
              <a :href="`#/editarmse/${registro.id}`" class="btn btn-soft btn-primary">
                <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" viewBox="0 0 512 512" fill="currentColor">
                  <path
                    d="M471.6 21.7c-21.9-21.9-57.3-21.9-79.2 0L362.3 51.7l97.9 97.9 30.1-30.1c21.9-21.9 21.9-57.3 0-79.2L471.6 21.7zm-299.2 220c-6.1 6.1-10.8 13.6-13.5 21.9l-29.6 88.8c-2.9 8.6-.6 18.1 5.8 24.6s15.9 8.7 24.6 5.8l88.8-29.6c8.2-2.7 15.7-7.4 21.9-13.5L437.7 172.3 339.7 74.3 172.4 241.7zM96 64C43 64 0 107 0 160L0 416c0 53 43 96 96 96l256 0c53 0 96-43 96-96l0-96c0-17.7-14.3-32-32-32s-32 14.3-32 32l0 96c0 17.7-14.3 32-32 32L96 448c-17.7 0-32-14.3-32-32l0-256c0-17.7 14.3-32 32-32l96 0c17.7 0 32-14.3 32-32s-14.3-32-32-32L96 64z" />
                </svg>
              </a>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <!-- modal para cada item -->
    <dialog v-for="(registro, id) in dadosFiltrados" :id="`modal-${id}`" :key="`modal-${id}`" class="modal">

      <div class="modal-box text-left">
        <form method="dialog">
          <button class="btn btn-soft btn-primary btn-sm btn-square absolute right-2 top-2">
            <svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4" viewBox="0 0 384 512" fill="currentColor">
              <path d="M342.6 150.6c12.5-12.5 12.5-32.8
             0-45.3s-32.8-12.5-45.3 0L192 210.7
             86.6 105.4c-12.5-12.5-32.8-12.5-45.3
             0s-12.5 32.8 0 45.3L146.7 256
             41.4 361.4c-12.5 12.5-12.5 32.8
             0 45.3s32.8 12.5 45.3 0L192 301.3
             297.4 406.6c12.5 12.5 32.8 12.5
             45.3 0s12.5-32.8 0-45.3L237.3 256
             342.6 150.6z" />
            </svg>
          </button>


        </form>


        <h3 class="font-bold text-lg mb-2">Detalhes da MSE</h3>


        <p><strong>ID:</strong> {{ registro.id }}</p>
        <p><strong>Processo:</strong> {{ registro.processo_num }}</p>
        <p><strong>Ato Infracional:</strong> {{ registro.infracao.nome }}</p>
        <p><strong>Tipo de MSE:</strong>{{ formatarTipoMse(registro.tipo_mse) }}</p>
        <p><strong>ID Adolescente:</strong> {{ registro.id_adolescente.nome }}</p>
        <p><strong>ID Orientador:</strong> {{ registro.id_orientador.nome }}</p>
        <p><strong>Data de Início:</strong> {{ registro.data_inicio }}</p>
        <p><strong>Data de Fim:</strong> {{ registro.data_fim }}</p>


        <strong>Situação:</strong>

        <span :class="registro.concluida ? 'text-red-500 font-semibold' : 'text-green-600 font-semibold'">
          {{ registro.concluida ? 'Finalizada' : 'Vigente' }}
        </span>

        <p v-if="registro.concluida && registro.tipo_finalizacao !== null">
          <strong>Tipo de Finalização:</strong> {{ formatarFinalizacao(registro.tipo_finalizacao) }}
        </p>

        <p v-if="registro.concluida && registro.tipo_finalizacao === 1 && registro.tipo_interrupcao !== null">
          <strong>Tipo de Interrupção:</strong> {{ formatarInterrupcao(registro.tipo_interrupcao) }}
        </p>
        <p><strong>Número da Caixa Baixa:</strong> {{ registro.caixa_baixa_num }}</p>
      </div>
    </dialog>
  </div>
</template>


<script setup>
import { ref, computed, onMounted } from 'vue'  //acessa elementos e renderizar atualizando
import axios from 'axios'
const dados = ref([]) //cria uma lista vazia
const filtro = ref('') //filtro da busca
const statusSelecionado = ref('') //mostrar os status filtados
const anoSelecionado = ref('')  //mostrar os anos selecionados
const anosDisponiveis = ref([]) //mostrar na barra de seleção só anos cadastrados
const campoBusca = ref('')
const apiFiltro = 'http://127.0.0.1:8000/api/mse/filtro'


onMounted(() => {
  axios.get('http://127.0.0.1:8000/api/mse/')
    .then((response) => {
      dados.value = response.data


      const anos = new Set()
      dados.value.forEach(reg => {
        const ano = new Date(reg.data_inicio).getFullYear()
        anos.add(ano)
      })
      anosDisponiveis.value = Array.from(anos).sort((a, b) => b - a)
    })
    .catch((error) => {
      console.error('Erro ao buscar MSEs:', error)
    })
})



//função por abrir o modal de visualização
function abrirModal(id) {
  document.getElementById(`modal-${id}`).showModal()
}


//conjunto de funções para formatação
function formatarTipoMse(tipo) {
  return tipo === 0 ? 'Liberdade Assistida (LA)' :
    tipo === 1 ? 'Prestação de Serviços à Comunidade (PSC)' :
      'LA com PSC'
}


function formatarFinalizacao(tipo) {
  if (tipo === null || tipo === undefined) return ''
  return tipo === 0 ? 'Concluída' :
    tipo === 1 ? 'Interrompida' :
      tipo === 2 ? 'Transferida' :
        tipo === 3 ? 'Regredida' :
          'Desconhecido'
}



function formatarInterrupcao(tipo) {
  return tipo === 0 ? 'Case' :
    tipo === 1 ? 'PRSM ou outra penitenciária' :
      tipo === 2 ? 'Desistência' :
        tipo === 3 ? 'Extinta pelo Judiciário (prescrição)' :
          tipo === 4 ? 'Idade' :
            'Revogada (não cumpre)'
}


//função responsavel pelo filtro dos dados
const dadosFiltrados = computed(() => {
  return dados.value.filter(registro => {
    const textoBusca = filtro.value.toLowerCase()


    const buscaOk =
      registro.processo_num?.toString().toLowerCase().includes(textoBusca) ||
      registro.infracao?.nome?.toLowerCase().includes(textoBusca) ||
      registro.id_adolescente?.nome?.toLowerCase().includes(textoBusca)


    const statusOk =
      statusSelecionado.value === ''
        ? true
        : statusSelecionado.value === 'vigente'
          ? !registro.concluida
          : registro.concluida


    const anoOk =
      anoSelecionado.value === ''
        ? true
        : new Date(registro.data_inicio).getFullYear().toString() === anoSelecionado.value


    return buscaOk && statusOk && anoOk
  })
})

//função responsavel por aplicar a busca digitada
function aplicarBusca() {
  filtro.value = campoBusca.value.trim()
}


//função responsavel por limpar os filtros
function limparFiltros() {
  campoBusca.value = ''
  filtro.value = ''
  anoSelecionado.value = ''
  statusSelecionado.value = ''
}
</script>
