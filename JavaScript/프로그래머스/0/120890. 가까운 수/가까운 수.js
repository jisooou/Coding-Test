function solution(array, n) {
    let answer = 0;
    
    let min = 99999999;
    
    const arraySort = array.sort((a,b) => a-b);
    
    for(let i = 0; i<arraySort.length; i++){
        const num = arraySort[i];
        if(min > Math.abs(n - num)){
            min = Math.abs(n - num);
            answer = num;
        }
    }
    return answer;
}