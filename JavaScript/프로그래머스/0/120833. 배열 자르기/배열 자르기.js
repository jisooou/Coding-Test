function solution(numbers, num1, num2) {
    var answer = [];
    answer= numbers.slice(num1, num2+1);
    //slice 함수는 잘라낼 배열의 시작index와 end index를 파라미터로 받아서, 그 사이의 원소들을 새로운 배열로 만들어 리턴한다. 
    return answer;
}