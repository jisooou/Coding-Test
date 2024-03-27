//1번째 풀이 

function solution(order){
    var answer = 0; 
    
    //문자열로 바꿔주기 
    const numbers = order.toString();
    
    for(let i = 0; i < numbers.length; i++){
        if(numbers[i] == 3 || numbers[i] == 6 || numbers[i] == 9){
            answer = answer + 1;
        }
    }
    
    return answer;
}

//--------------------------------------------------------------//
//2번째 풀이 

//스프레드 연산자 
//forEach() 함수

/*
function solution(order){
    var answer = 0; 
    
    [...String(order)].forEach(number => {
        if(number == 3 || number == 6 || number == 9) answer++; 
    })
    
    return answer;
}
*/