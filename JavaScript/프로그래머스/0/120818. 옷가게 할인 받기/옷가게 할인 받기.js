//Math.floor : 소수점 버림 
//if문 사용할 때 바로 return 되지 않도록 주의 

function solution(price) {
    
    if(price >= 500000){
        return Math.floor(price * 0.8)
    }
    else if(price >= 300000){
        return Math.floor(price * 0.9)
    }
    else if(price >= 100000){
        return Math.floor(price * 0.95)
    }
    else{
        return price;
    }
}