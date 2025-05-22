<template>
    <div class="super">
        <div class="text-div">
            <h1> Bem-vindo ao BDedica</h1>
            <p> Sistema para cadastro, visualização e edição de medidas socioeducativas e adolescentes para controle do Centro de Defesa dos Direitos da Criança e do Adolescente de Santa Maria</p>
        </div>
        <form>
            <h1>Entre no sistema</h1>
            <div class="campo">
                <label for="email">Seu e-mail</label>
                <input type="email" id="email" required/>
                <label for="password">Sua senha</label>
                <input type="password" id="password" required />
            </div>
            <button class="btn" id="btn" @click="logar">Entrar</button>
        </form>
    </div>
</template>
    
<script>
export default {
  name: 'telaLogin',

  methods: {
    logar(){
        const email = document.getElementById('email').value;
        const senha = document.getElementById('password').value;
    
        if (email == 'teste@gmail.com' && senha == 'teste'){
            window.location.hash = '/consulta';
        } else {
            alert('erro')
        }
    }
  }
}

</script>

<style scoped>
   .super {
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: center;
        padding: 50px;
        gap: 50px;
        flex-wrap: wrap;
    }

    h1 {
        font-size: 28px;
    }

    .text-div {
        flex: 1;
        min-width: 300px;
        max-width: 500px;
    }

    form {
        flex: 1;
        min-width: 300px;
        max-width: 400px;
        display: flex;
        flex-direction: column;
        border: 2px solid;
        border-radius: 20px;
        padding: 20px;
        gap: 25px;
        background-color: rgb(218, 203, 173);
    }

    .campo {
        display: flex;
        flex-direction: column;
        gap: 5px;
    }

    input {
        padding: 10px 20px;
        border-radius: 20px;
        background-color: rgb(71, 54, 49);
        color: white;
        border: none;
    }

    label {
        text-align: left;
    }

    @media (max-width: 768px) {
        .super {
            flex-direction: column;
            align-items: stretch;
            padding: 20px;
        }

        .text-div, form {
            max-width: 100%;
        }
    }

</style>