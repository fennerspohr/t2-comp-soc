<template>
  <div class="p-4">
    <h1 class="text-2xl font-bold mb-4">Consulta de Medidas</h1>
    <div class="overflow-x-auto">
      <table class="table table-zebra w-full">
        <!-- Cabeçalho -->
        <thead>
          <tr>
            <th>Nome</th>
            <th>Sexo</th>
            <th>Início MSE</th>
            <th>Fim MSE</th>
            <th>Ato Infracional</th>
          </tr>
        </thead>
        <!-- Corpo da Tabela -->
        <tbody>
          <tr v-for="(registro, id) in dados" :key="id"> <!--pra cada item de dados cria uma tabela usando registro como variavel e id como posição do item-->
            <td>{{ registro.nome }}</td>
            <td>{{ registro.sexo }}</td>
            <td>{{ registro.inicio_mse }}</td>
            <td>{{ registro.fim_mse }}</td>
            <td>{{ registro.ato_infracional }}</td>
            <td>
              <button class="btn btn-sm" @click="abrirModal(id)">view</button>  <!--cria o botao como um item de cada linha que ao ser clicado abre o modal-->
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
          <button class="btn btn-sm btn-circle btn-ghost absolute right-2 top-2">✕</button>
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

onMounted(() => {
  dados.value = teste //ao carregar a pagina preenche os dados com o JSON
})

function abrirModal(id) {
  const modal = document.getElementById(`modal-${id}`)
  if (modal) {
    modal.showModal()
  }
}

</script>

<style scoped>
</style>
