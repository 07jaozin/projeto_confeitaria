const container = document.querySelector('.container');
const registerBtn = document.querySelector('.register-btn');
const tel = document.querySelectorAll('.tel');
const inputs = document.querySelectorAll('.input');

registerBtn.addEventListener("click", () => {
    window.location.href='/carrinho'
})

let total_input = 0;  
let todos_botoes = document.querySelectorAll('.tel');
todos_botoes.forEach( botao => {
botao.addEventListener("keydown", function(event){
    const teclasPermitidas = ["Backspace", "Delete", "ArrowLeft", "ArrowRight", "Tab"];

    if (!event.key.match(/[0-9]/) && !teclasPermitidas.includes(event.key)) {
        event.preventDefault();
}
    else if(event.key === " "){
        event.preventDefault();
    }
});
});
document.addEventListener("DOMContentLoaded", function() {
    const nomeLogin = document.getElementById('nome-login');
    const telefoneLogin = document.getElementById('telefone-login');
    const btnEntrar = document.getElementById('btn-entrar');
    
    

   
    telefoneLogin.addEventListener("input", (event) => {
        let input = event.target.value;

    input = input.replace(/\D/g, '');

    if (input.length <= 2) {
        input = `(${input}`;
    } else if (input.length <= 7) {
        input = `(${input.slice(0, 2)}) ${input.slice(2)}`;
    } else if (input.length <= 10) {
        input = `(${input.slice(0, 2)}) ${input.slice(2, 7)}-${input.slice(7)}`;
    } else {
        input = `(${input.slice(0, 2)}) ${input.slice(2, 7)}-${input.slice(7, 11)}`;
    }

    event.target.value = input;
    });
    function validarTelefone(telefone) {
        return telefone.length === 15;
    }

   
    function verificarCampos() {
        
        if (nomeLogin.value && telefoneLogin.value && validarTelefone(telefoneLogin.value)) {
            btnEntrar.disabled = false;
            btnEntrar.classList.remove('desabilitado');
        } else {
            btnEntrar.disabled = true;
            btnEntrar.classList.add('desabilitado');

        };

    }

    nomeLogin.addEventListener('input', verificarCampos);
    telefoneLogin.addEventListener('input', verificarCampos);
   

    verificarCampos();
});

