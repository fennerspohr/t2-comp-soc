<script setup>
import HelloWorld from './components/HelloWorld.vue'
import Cadastro from './Cadastro.vue'
import { ref, computed } from 'vue'
import Navbarteste from './components/navbarteste.vue'
import listamse from './listamse.vue'
import telaLogin from './telaLogin.vue'
import CadastroAdolescente from './CadastroAdolescente.vue'
import listaAdolescentes from './lista-adolescentes.vue'
import cadastromse from './cadastromse.vue'

const routes = {  //aqui a gente atribui um componente ou pagina pra uma url
  '/': telaLogin,
  '/about': Cadastro,
  '/about/cadastro-adolescente': CadastroAdolescente,
  '/listamse': listamse,
  '/lista-adolescentes': listaAdolescentes, 
  '/about/cadastromse': cadastromse,
}

const currentPath = ref(window.location.hash) //pega o path atual, que eh o que fica depois da # na url (antes de clicar nos botoes nao tem # nenhuma pq eh a url inicial)

window.addEventListener('hashchange', () => { //fica assistindo a # da url e quando a rota muda, altera o currentPath
  currentPath.value = window.location.hash
})

const currentView = computed(() => { //altear o currentView
  return routes[currentPath.value.slice(1) || '/'] //seleciona a rota de acordo com a string do currentPath
})


</script>

<template>
  <Navbarteste></Navbarteste> <!-- o que estiver nesse template vai ser exibido independente da url-->
  <component :is="currentView" /> <!--Aqui é exibido o conteudo da view correspondente -->
</template>

<style>
#app {
  font-family: 'Roboto', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 0px;
}

body {
  padding: 0 !important;
  margin: 0 !important;
 }
</style>