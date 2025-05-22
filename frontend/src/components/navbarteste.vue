<template>
  <header class="navbar bg-base-200 px-6 shadow-md">
    <div class="flex-1">
      <a class="btn btn-ghost normal-case text-3xl font-bold text-primary">BDedica</a>
    </div>

    <nav class="flex-none">
      <ul class="menu menu-horizontal px-1 text-base-content">

        <li><a href="#/about" class="hover:text-primary hover-secondary-focus ">Cadastro</a></li>
        <li><a href="#/listamse" class="hover:text-primary">MSEs</a></li>
        <li><a href="#/lista-adolescentes" class="hover:text-primary:">Adolescentes</a></li>
      </ul>
    </nav>

    <div class="ml-4">
      <img src="../assets/criancas.png" alt="Logo Crianças" class="w-16 h-16 rounded-md object-cover" />
    </div>
  </header>
</template>

<script>
export default {
  name: 'Navbarteste',
}
</script>

<style scoped>

</style>
