//================ REMOVE ITEM ====================

document.addEventListener("DOMContentLoaded", () => {
    const remove_botao = document.querySelectorAll('.trash');
    

    remove_botao.forEach(botao => {
        
        botao.addEventListener("click", () => {
            let id = parseInt(botao.getAttribute('data-id'));
            fetch('/exclui_carrinho', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(id)
            })
            .then(() => {
                window.location.href = '/carrinho';
            });
        });
    });
});

//=============== SHOW MENU ===============


const navMenu = document.getElementById('nav-menu'),
      navToggle = document.getElementById('nav-toggle'),
      navClose = document.getElementById('nav-close')

/* Menu show */
if(navToggle){
    navToggle.addEventListener('click', () =>{
        navMenu.classList.add('show-menu')
    })
}

/* Menu hidden */
if(navClose){
    navClose.addEventListener('click', () =>{
        navMenu.classList.remove('show-menu')
    })
}

//=============== REMOVE MENU MOBILE ===============
const navLink = document.querySelectorAll('.nav__link')

const linkAction = () =>{
    const navMenu = document.getElementById('nav-menu')
    navMenu.classList.remove('show-menu')
}
navLink.forEach(n => n.addEventListener('click', linkAction))

//=============== CHANGE BACKGROUND HEADER ===============
const blurHeader = () =>{
    const header = document.getElementById('header')
    this.scrollY >= 50 ? header.classList.add('blur-header') 
                       : header.classList.remove('blur-header')
}
window.addEventListener('scroll', blurHeader)

   







//=============== animação link ===============

const sections = document.querySelectorAll('section[id]')
    
const scrollActive = () =>{
  	const scrollDown = window.scrollY

	sections.forEach(current =>{
		const sectionHeight = current.offsetHeight,
			  sectionTop = current.offsetTop - 58,
			  sectionId = current.getAttribute('id'),
			  sectionsClass = document.querySelector('.nav__menu a[href*=' + sectionId + ']')

		if(scrollDown > sectionTop && scrollDown <= sectionTop + sectionHeight){
			sectionsClass.classList.add('active-link')
		}else{
			sectionsClass.classList.remove('active-link')
		}                                                    
	})
}
window.addEventListener('scroll', scrollActive)
/*=============== ADD CARD ===============*/

const add__line = document.querySelectorAll('.add__line__card');
const subtract__line = document.querySelectorAll('.subtract__line__card');
const quant__item = document.querySelectorAll('.quant__item__card');


add__line.forEach((button, index) => {
    button.addEventListener("click", () => {
        
        let value = parseInt(quant__item[index].innerText);
        quant__item[index].innerText = value + 1;
        let quant = quant__item[index].innerText = value + 1;
        let id = parseInt(button.getAttribute('data-id'));
        subtract__line[index].style.color = ' hsl(28, 88%, 62%)';
        let lista = [];
        let item = {
            'id': id,
            'quantidade': quant

        };
        lista.push(item)

        fetch('/atualiza_carrinho',{
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(lista)}
    
        )
    })

})

subtract__line.forEach((button, index) => {
    button.addEventListener("click", () => {
        let value = parseInt(quant__item[index].innerText);
        total = total + value;
        
        if(value > 1){
        
        quant__item[index].innerText = value - 1;
        if(value - 1  === 1){
            button.style.color = 'gray';
        };
        let quant = quant__item[index].innerText = value - 1;
        let id = parseInt(button.getAttribute('data-id'));
        let lista = [];
        let item = {
            'id': id,
            'quantidade': quant

        };
        lista.push(item)
        
        fetch('/atualiza_carrinho',{
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(lista)}
    
        )
    

        
        }
       
    })
})
const add__line__index = document.querySelectorAll('.add__line');
const subtract__line__index = document.querySelectorAll('.subtract__line');
const quant__item__index = document.querySelectorAll('.quant__item');
const favorite__price = document.querySelectorAll('.favorite__price span');
const total_pagar = document.querySelector('.total_pagar');

let total = 0;

add__line__index.forEach((button, index) => {
    button.addEventListener("click", () => {
        add_id_ovo(button, index);

        let value = parseInt(quant__item__index[index].innerText);
        quant__item__index[index].innerText = value + 1;
        total += 1;

        let valor = parseFloat(total_pagar.innerText.replace(",", "."));
        let preco = parseFloat(favorite__price[index].innerText.replace(",", "."));
        let novoTotal = (preco + valor).toFixed(2).replace(".", ",");
        total_pagar.innerText = novoTotal;

        button.style.color = 'hsl(28, 88%, 62%)';
        
        const add = document.querySelector('.add__container');
        if (total > 0) {
            add.classList.add('visible');
        }
    });
});

subtract__line__index.forEach((button, index) => {
    button.addEventListener("click", () => {
        let value = parseInt(quant__item__index[index].innerText);
        subtract_id_ovo(button, index);

        if (value > 0) {
            quant__item__index[index].innerText = value - 1;
            total -= 1;

            let valor = parseFloat(total_pagar.innerText.replace(",", "."));
            let preco = parseFloat(favorite__price[index].innerText.replace(",", "."));
            let novoTotal = (valor - preco).toFixed(2).replace(".", ",");
            total_pagar.innerText = novoTotal;
        } else {
            button.style.color = 'gray';
        }

        const add = document.querySelector('.add__container');
        if (total > 0) {
            add.classList.add('visible');
        } else {
            add.classList.remove('visible');
        }
    });
});


let carrinho = []
function add_id_ovo(element, index){
    let id = parseInt(element.getAttribute('data-id'));
    
    let quant = parseInt(quant__item__index[parseInt(index)].innerText) + 1;
    let encontrado = false

    for(let i = 0; i < carrinho.length; i++){
        if(carrinho[i].id === id){
            carrinho[i]['quantidade'] = quant;
            encontrado = true;
            break
        }
    }

    if(!encontrado){
        novo_item = {'id' : parseInt(id),
                    'quantidade': quant}
        carrinho.push(novo_item)
    }
   
}
function subtract_id_ovo(element, index){
    let id = parseInt(element.getAttribute('data-id'));
    if(carrinho.length > 0){
    let quant = parseInt(quant__item__index[parseInt(index)].innerText) - 1;
    let encontrado = false;

    
    for(let i = 0; i < carrinho.length; i++){
        if(carrinho[i].id === id){
            if(quant > 0){
            carrinho[i]['quantidade'] = quant;
            }
            else if( quant == 0){
                carrinho.splice(i, 1);
            };
            encontrado = true;
            break
        }
    }
   
    
    
    }
   
   
}

const add__button = document.querySelector('.add__button');

add__button.addEventListener("click", () =>{
    fetch('/adiciona_carrinho', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(carrinho)
    }
    )
    .then( () =>{
        window.location.href = '/carrinho'
    })
})

