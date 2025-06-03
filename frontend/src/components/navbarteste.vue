<template>
  <header class="navbar bg-base-200 px-40 shadow-md">
    <!-- Logo + nome -->
    <div class="flex items-center gap-0">
      <img 
        src="../assets/criancas.png" 
        alt="Logo Crianças" 
        class="w-12 h-12 rounded-md object-cover"
      />
      <a 
        href="#/" 
        class="btn btn-link link-hover text-2xl font-bold text-primary"
      >
        BDedica
      </a>
    </div>

    <!-- Menu - aparece só se estiver logado -->
    <nav class="flex-1 justify-left" v-if="isLogado">
      <ul class="menu menu-horizontal px-1 text-base-content">
        <li><a href="#/listamse" class="hover:text-primary">MSEs</a></li>
        <li><a href="#/lista-adolescentes" class="hover:text-primary">Adolescentes</a></li>
        <li><a href="#/about" class="hover:text-primary">Cadastro</a></li>
      </ul>
    </nav>

    <!-- Login / Logout -->
    <div>
      <button 
        class="btn btn-soft btn-primary gap-1"
        @click="fazerLoginLogout"
      >
        <!-- Ícone -->
        <svg xmlns="http://www.w3.org/2000/svg" 
          viewBox="0 0 448 512" 
          fill="currentColor" 
          class="w-4 h-4"
        >
          <path 
            d="M224 256A128 128 0 1 0 224 0a128 128 0 1 0 0 256zm-45.7 48C79.8 304 0 383.8 0 482.3C0 498.7 13.3 512 29.7 512l388.6 0c16.4 0 29.7-13.3 29.7-29.7C448 383.8 368.2 304 269.7 304l-91.4 0z"/>
        </svg>
        {{ isLogado ? 'Logout' : 'Login' }}
      </button>
    </div>
  </header>
</template>

<script>
export default {
  name: 'Navbarteste',
  data() {
    return {
      isLogado: false, //simulação de login
    }
  },
  methods: {
    fazerLoginLogout() {
      if (this.isLogado) {
        //faz logout e redireciona para "/"
        this.isLogado = false;
        window.location.hash = '#/';
      } else {
        //faz login (simulado)
        this.isLogado = true;
      }
    }
  }
}
</script>

<style scoped>
</style>
