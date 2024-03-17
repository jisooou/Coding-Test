function solution(n) {
    var answer = 0;
    n = String(n);
    n = n.split("");
    
    for (let i = 0; i < n.length; i++) {
        answer += parseInt(n[i]);
    }
    return answer;
}