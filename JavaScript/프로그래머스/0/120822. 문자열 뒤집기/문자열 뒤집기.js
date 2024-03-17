function solution(my_string) {
    var answer = '';
    answer = my_string.split('').reverse().join('');
    //answer는 my_string 문자열을 나누고 전체적으로 뒤집고 다시 문자열을 붙인다.
    return answer;
}