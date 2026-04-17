
let prev = document.getElementById('prev')
let curr = document.getElementById('curr')
let operationDisplay = document.getElementById('opration')

let firstValue = ""
let secondValue = ""
let operation = null

let sum=[]

function handleclick(value){
    
    if(typeof value === "number"){
        secondValue += value
        curr.innerText = secondValue
    }
    else if(value === "+" || value === "-" || value === "*" || value === "/"){
        if(secondValue === "") return

        firstValue = secondValue
        operation = value
        secondValue = ""

        prev.innerText = firstValue
        operationDisplay.innerText = operation
        curr.innerText = ""
    }
    else if(value === "="){
        calculate()
    }
}

function calculate(){
    let num1 = Number(firstValue)
    let num2 = Number(secondValue)
    let result = 0

    if(operation === "+"){
        result = num1 + num2
    }
    else if(operation === "-"){
        result = num1 - num2
    }
    else if(operation === "*"){
        result = num1 * num2
    }
    else if(operation === "/"){
        result = num1 / num2
    }

    curr.innerText = result
    prev.innerText = ""
    operationDisplay.innerText = ""

    secondValue = result.toString()
    firstValue = ""
    operation = null
}

function clearAll(){
    firstValue = ""
    secondValue = ""
    operation = null

    prev.innerText = ""
    curr.innerText = ""
    operationDisplay.innerText = ""
}

function handleclick(value){
    if(typeof value == "number"){
        sum.append(value)
        return sum

    }else if(value === "+" || value === "-" || value === "*" || value === "/"){
        secondValue=sum
        
    }

}