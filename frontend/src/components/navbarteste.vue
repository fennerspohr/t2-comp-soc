<template>
        <header>
            <span class="logotipo"> BDedica</span>
            <nav class="nav-links">
                <ul>
                    <li><a href="#">Home</a></li>
                    <li><a href="#/about">Cadastro</a></li>
                    <li><a href="#/listamse">Lista MSE</a></li>
                </ul>
            </nav>
            <img src="../assets/criancas.png" width="100px" height="100px">
        </header>
</template>

<script>

export default {
  name: 'Navbarteste',
}

</script>

<style scoped>
    li, a {
        font-size: 20px;
        color: rgba(0, 0, 0, 0.411);
        text-decoration: none;
    }
    header {
        margin: 0px;
        display: flex;
        justify-content: flex-end;
        align-items: center;
        padding: 10px;
        background-color: rgb(218, 203, 173);
        position: relative;
    }
    .logotipo {
        color: rgb(71, 54, 49);
        font-size: 35px;
        font-weight: bold; 
        margin-right: auto;  
    }
    .nav-links {
        list-style: none;
    }
    .nav-links li {
        display: inline-block;
        padding: 0px 20px;
    }
    .nav-links li a:hover{
        color: rgb(0, 0, 0);
    }

</style>