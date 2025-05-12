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
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'  //acessa elementos e renderizar atualizando
import teste from './teste.json'  //importa os dados do json

const dados = ref([]) //cria uma lista vazia

onMounted(() => {
  dados.value = teste //ao carregar a pagina preenche os dados com o JSON
})
</script>

<style scoped>
</style>
