//스프레드 연산자 
//forEach() 함수

function solution(order){
    let answer = 0; 
    
    [...String(order)].forEach(number => {
        if(number == 3 || number == 6 || number == 9) answer++; 
    })
    
    return answer;
}