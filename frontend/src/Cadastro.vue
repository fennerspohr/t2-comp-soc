<template>
  <div class="min-h-screen flex flex-col md:flex-row items-center justify-center gap-10 p-6 bg-base-100">
    <a href="#/about/cadastromse" class="card bg-primary w-96 shadow-sm p-5 cursor-pointer hover:shadow-lg transition">
      <figure>
        <img class="w-1/3 h-1/3" src="./assets/mseicone.png" alt="icone medida">
      </figure>
      <div class="card-body flex items-center justify-center">
        <h2 class="card-title text-center text-primary-content">Cadastro MSE</h2>
      </div>
    </a>

    <a href="#/about/cadastro-adolescente" class="card bg-secondary w-96 shadow-sm p-5 cursor-pointer hover:shadow-lg transition">
      <figure>
        <img class="w-1/3 h-1/3" src="./assets/adolescenteicone.png" alt="icone adolescente">
      </figure>
      <div class="card-body flex items-center justify-center">
        <h2 class="card-title text-center text-secondary-content-100">Cadastro de Adolescente</h2>
      </div>
    </a>
  </div>
</template>

<script>

  export default {
  name: 'Cadastro',
}
  </script>
  
  <style>
  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
  }
  </style>