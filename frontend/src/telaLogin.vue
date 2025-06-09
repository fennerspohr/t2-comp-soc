<template>
  <div class="min-h-screen flex flex-col md:flex-row items-center justify-center gap-10 p-6 bg-base-100">
    
    <div class="max-w-md text-center md:text-left space-y-4">
      <h1 class="text-3xl font-bold text-primary">Bem-vindo ao BDedica</h1>
      <p class="text-base-content">
        Sistema para cadastro, visualização e edição de medidas socioeducativas e adolescentes para controle do
        Centro de Defesa dos Direitos da Criança e do Adolescente de Santa Maria.
      </p>
    </div>

    <form @submit.prevent="logar" class="w-full max-w-sm bg-base-200 rounded-box p-6 shadow-md space-y-4">
      <h2 class="text-2xl font-semibold text-center text-base-content">Entre no sistema</h2>

      <div class="form-control">
        <label class="label" for="email">
          <span class="label-text">Seu e-mail</span>
        </label>
        <input type="email" id="email" v-model="email" class="input input-bordered" required />
      </div>

      <div class="form-control">
        <label class="label" for="password">
          <span class="label-text">Sua senha</span>
        </label>
        <input type="password" id="password" v-model="senha" class="input input-bordered" required />
      </div>

      <button type="submit" class="btn btn-primary w-full">Entrar</button>
    </form>

  </div>
</template>

<script>
import { isLogged } from './estadoLogin'

export default {
  name: 'TelaLogin',
  data() {
    return {
      email: '',
      senha: ''
    }
  },
  methods: {
    logar() {
      if (this.email === 'teste@gmail.com' && this.senha === 'teste') {
        isLogged.value = true
        window.location.hash = '/home'
      } else {
        alert('E-mail ou senha incorretos.')
      }
    }
  }
}
</script>

<style scoped>

</style>
