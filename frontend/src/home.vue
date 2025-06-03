<template>
  <div class="flex flex-col items-center justify-center min-h-screen gap-8 bg-base-100">

    <!-- Dashboard -->
    <div class="stats shadow">
      <div class="stat">
        <div class="stat-figure text-secondary">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
            class="inline-block h-8 w-8 stroke-current">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
              d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z">
            </path>
          </svg>
        </div>
        <div class="stat-title">MSE Vigentes</div>
        <div class="stat-value">8</div>
        <div class="stat-desc">Atualizado hoje</div>
      </div>

      <div class="stat">
        <div class="stat-figure text-secondary">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
            class="inline-block h-8 w-8 stroke-current">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
              d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4">
            </path>
          </svg>
        </div>
        <div class="stat-title">MSE Finalizadas</div>
        <div class="stat-value">15</div>
        <div class="stat-desc">↗︎ 2 (última semana)</div>
      </div>

      <div class="stat">
        <div class="stat-figure text-secondary">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
            class="inline-block h-8 w-8 stroke-current">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
              d="M5 8h14M5 8a2 2 0 110-4h14a2 2 0 110 4M5 8v10a2 2 0 002 2h10a2 2 0 002-2V8m-9 4h4">
            </path>
          </svg>
        </div>
        <div class="stat-title">Adolescentes</div>
        <div class="stat-value">12</div>
        <div class="stat-desc">↘︎ 1 (este mês)</div>
      </div>
    </div>

    <!-- Alertas e Dados da MSE -->
    <div class="flex flex-col items-center justify-center gap-3">

      <!-- Alerta de atraso -->
      <div v-if="diasRestantes <= 0" class="alert alert-error w-fit">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 shrink-0 stroke-current" fill="none"
          viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
            d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 
            2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z" />
        </svg>
        <span>⚠️ Atenção! Esta MSE está <strong>atrasada</strong>.</span>
      </div>

      <!-- Alerta de próximo ao vencimento -->
      <div v-else-if="diasRestantes <= 7" class="alert alert-warning w-fit">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 shrink-0 stroke-current" fill="none"
          viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
            d="M12 9v2m0 4h.01m-6.938 
            4h13.856c1.54 0 2.502-1.667 
            1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 
            0L3.34 16c-.77 1.333.192 3 1.732 3z" />
        </svg>
        <span>🔔 Aviso! Faltam <strong>{{ diasRestantes }}</strong> dias para o término da MSE.</span>
      </div>

      <!-- Dentro do prazo -->
      <div v-else class="alert alert-success w-fit">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 shrink-0 stroke-current" fill="none"
          viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
            d="M5 13l4 4L19 7" />
        </svg>
        <span>MSE dentro do prazo. Faltam <strong>{{ diasRestantes }}</strong> dias.</span>
      </div>

      <!-- Card de dados da MSE -->
      <div class="card bg-base-100 shadow-xl w-fit">
        <div class="card-body">
          <h2 class="card-title">Dados da MSE</h2>
          <p><strong>Adolescente:</strong> {{ mse.nome }}</p>
          <p><strong>Data de término:</strong> {{ mse.dataTermino }}</p>
        </div>
      </div>

    </div>
  </div>
</template>


<script setup>
import { ref, computed } from 'vue'

const mse = ref({
  nome: 'João Silva',
  dataTermino: '2025-06-10' 
})

const diasRestantes = computed(() => {
  const hoje = new Date()
  const termino = new Date(mse.value.dataTermino + 'T23:59:59')
  const diff = (termino - hoje) / (1000 * 60 * 60 * 24)
  return Math.ceil(diff)
})
</script>
