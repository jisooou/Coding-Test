function solution(n) {
    var answer = 0;
    for(var i =0 ; i<=n ; i++){
        if(i%2==0){
            answer+=i
        }        
    }

     //for (;n>0;n--){
       // console.log(n)
    //}

    return answer;
}