<script setup>
import Cadastro from './Cadastro.vue'
import { ref, computed } from 'vue'
import navbar from './components/navbar.vue'
import telaLogin from './telaLogin.vue'
import CadastroAdolescente from './CadastroAdolescente.vue'
import listaAdolescentes from './lista-adolescentes.vue'
import cadastromse from './cadastromse.vue'
import editarmse from './editarmse.vue'
import editarAdolescente from './editar-adolescente.vue'
import unidades from './unidades.vue'
import cam from './components/cam.vue'

const routes = {  //aqui a gente atribui um componente ou pagina pra uma url
  '/': telaLogin,
  '/about': Cadastro,
  '/about/cadastro-adolescente': CadastroAdolescente,
  '/lista-adolescentes': listaAdolescentes, 
  '/about/cadastromse': cadastromse,
  '/editarmse/:id': editarmse,  //rota pra edição com o id
  '/editar-adolescente/:id': editarAdolescente,
  '/unidades': unidades,
  '/cam': cam,
}

const currentPath = ref(window.location.hash) //pega o path atual, que eh o que fica depois da # na url (antes de clicar nos botoes nao tem # nenhuma pq eh a url inicial)

window.addEventListener('hashchange', () => { //fica assistindo a # da url e quando a rota muda, altera o currentPath
  currentPath.value = window.location.hash
})

const currentView = computed(() => {
  const path = currentPath.value.slice(1) || '/'

  //verifica se existe uma rota exata
  if (routes[path]) {
    return routes[path]
  }

  //verifica se eh uma rota dinamica
  //se começar com editarmse retorna o componente de id 
  if (path.startsWith('/editarmse/')) {
    return routes['/editarmse/:id']
  }

  //se começar com editar-adolescente retorna o componente de id
  if (path.startsWith('/editar-adolescente/')) {
    return routes['/editar-adolescente/:id']
  }

  return null
})



</script>

<template>
  <navbar></navbar> <!-- o que estiver nesse template vai ser exibido independente da url-->
  <component :is="currentView" /> <!--Aqui é exibido o conteudo da view correspondente -->
  <cam></cam>
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