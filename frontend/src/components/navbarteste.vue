<template>
  <header class="navbar bg-base-200 px-40 shadow-md">
    <!-- Logo + nome -->
    <div class="flex items-center gap-0">
      <img 
        src="../assets/criancas.png" 
        alt="Logo Crianças" 
        class="w-12 h-12 rounded-md object-cover"
      />
      <a v-if="isLogged"
        href="#/home" 
        class="btn btn-link link-hover text-2xl font-bold text-primary"
      >
        BDedica
      </a>
      <a v-if="!isLogged" class="btn btn-link link-hover text-2xl font-bold text-primary" >
        BDedica
      </a> 
    </div>

    <!-- Menu - aparece só se estiver logado -->
    <nav class="flex-1 justify-left" v-if="isLogged">
      <ul class="menu menu-horizontal px-1 text-base-content">
        <li><a href="#/listamse" class="hover:text-primary">MSEs</a></li>
        <li><a href="#/lista-adolescentes" class="hover:text-primary">Adolescentes</a></li>
        <li><a href="#/about" class="hover:text-primary">Cadastro</a></li>
      </ul>
    </nav>

    <!-- Logout -->
    <div v-if="isLogged">
      <button 
        class="btn btn-soft btn-primary gap-1"
        @click="fazerLogout"
      >
        Sair da conta
      </button>    
    </div>
  </header>
</template>

<script setup>
import { isLogged } from '../estadoLogin'

function fazerLogout() {
  isLogged.value = false
  window.location.hash = '#/'
}
</script>
