<template>
  <header class="navbar flex justify-between items-center bg-base-200 px-40 shadow-md">
    <!-- Logo + nome --> 
    <div class="flex items-center gap-0">
      <img 
        src="../assets/logo.webp" 
        alt="Logo" 
        class="w-12 h-12 rounded-md object-cover"
      />
      <a v-if="isLogged"
        href="#/unidades" 
        class="btn btn-link link-hover text-2xl font-bold text-primary"
      >
        Voltron
      </a>
      <a v-if="!isLogged" class="btn btn-link link-hover text-2xl font-bold text-primary" >
        Voltron
      </a> 
    </div>

    <!-- Logout -->
    <div class = "flex-none">
    <div v-if="isLogged">
      {{ nomeUsuario }}
      <button 
        class="btn btn-soft btn-primary gap-1"
        @click="fazerLogout"
      >
        Sair da conta
      </button>  
    </div>
    </div>
  </header>
</template>

<script setup>
import { isLogged, nomeUsuario } from '../estadoLogin'

function fazerLogout() {
  isLogged.value = false
  window.location.hash = '#/'
}
</script>
