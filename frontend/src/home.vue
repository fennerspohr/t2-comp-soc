<script setup>
</script>

<template>
  <div class="min-h-screen bg-base-200 text-base-content px-8 py-12">
    <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-12 items-center">
      <!-- Lado do texto -->
      <div class="space-y-6">
        <h1 class="text-4xl font-bold text-primary">
          Sistema de Gestão de Medidas Socioeducativas
        </h1>
        <p class="text-lg text-gray-600 dark:text-gray-400">
          O BDedica — Banco de Dados do CEDEDICA — nasce como uma resposta direta a uma necessidade urgente: organizar, proteger e dar vida às informações de adolescentes atendidos por medidas socioeducativas (MSEs) em meio aberto.
        </p>

        <div class="card w-150 h-40 bg-primary text-primary-content">
  <div class="card-body">
    <p>O CEDEDICA é uma ONG que presta um trabalho essencial à comunidade, acompanhando jovens em cumprimento de medidas como Liberdade Assistida e Prestação de Serviços à Comunidade. No entanto, até então, essas informações eram armazenadas manualmente em cadernos, com dados incompletos, difíceis de consultar e impossíveis de filtrar rapidamente.</p>
  </div>
</div>
      </div>

      <!-- Lado da imagem + estatísticas -->
      <div class="flex flex-col items-center">
        <img class="w-full max-w-sm round " src="./assets/1089.png" alt="icone">
        
        <div class="stats shadow bg-base-100 w-full">
          <div class="stat">
            <div class="stat-title">Medidas Cadastradas</div>
            <div class="stat-value">+100</div>
          </div>
          <div class="stat">
            <div class="stat-title">Adolescentes Ativos</div>
            <div class="stat-value">25</div>
          </div>
          <div class="stat">
            <div class="stat-title">Orientadores Envolvidos</div>
            <div class="stat-value">8</div>
          </div>
        </div>
<p class="text-lg mt-5 text-gray-600 dark:text-gray-400">
Imagine tentar descobrir quantas meninas foram atendidas em 2023 ou quantas medidas foram iniciadas em abril — tudo isso exigia horas vasculhando folhas, anotando à mão, com risco de erro e perda de informações.

O BDedica resolve isso.
        </p>
        
      </div>
    </div>

    <!-- Rodapé -->
    <div class="mt-10 text-sm text-center text-gray-400">
      <p>Desenvolvido por Gustavo Pott, Isadora Spohr, Nathália Zófoli, Luiza Manoelle dos Santos – UFSM, Sistemas de Informação – CT 2025</p>
    </div>
  </div>
</template>
