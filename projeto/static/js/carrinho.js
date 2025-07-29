function calcularTotal() {
    const precos = document.querySelectorAll('.favorite__price span');
    const quantidades = document.querySelectorAll('.quant__item__card');
    const totalCampo = document.querySelector('#total-pagar');

    let total = 0;

    precos.forEach((precoElem, index) => {
        const preco = parseFloat(precoElem.innerText.replace(",", "."));
        const quantidade = parseInt(quantidades[index].innerText);
        total += preco * quantidade;
    });
    
    // Formata o total com vírgula no lugar do ponto
    totalCampo.innerText = `R$ ${total.toFixed(2).replace(".", ",")}`;
    }
    

    // Calcula total ao carregar a página
        document.addEventListener('DOMContentLoaded', calcularTotal);

    // Se quiser atualizar ao clicar nos botões de adicionar/subtrair:
    document.querySelectorAll('.add__line__card, .subtract__line__card').forEach(button => {
    button.addEventListener('click', () => {
        setTimeout(calcularTotal, 100);  // pequeno delay para esperar a alteração do DOM
     });
            });
    document.getElementById('enviar').addEventListener("click", () => {
        window.location.href = '/login';
    })
    document.getElementById('voltar').addEventListener("click", () =>{
     window.location.href = '/';
    })
