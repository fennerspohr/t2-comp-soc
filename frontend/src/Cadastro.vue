<template>
    <div class="min-h-screen flex flex-col md:flex-row items-center justify-center gap-10 pg-6 bg-base-100">
    <div class="card bg-secondary w-96 shadow-sm">
      <figure>
        <img class="w-1/3 h-1/3"
          src="./assets/mseicone.png">
      </figure>
      <div class="card-body">
        <h2 class="card-title">Cadastro de Medida</h2>
      </div>
    </div>

    <div class="card bg-accent w-96 shadow-sm">
      <figure>
        <img class="w-1/3 h-1/3"
          src="./assets/adolescenteicone.png">
      </figure>
      <div class="card-body">
        <h2 class="card-title">Cadastro de Adolescente</h2>
      </div>
    </div>
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