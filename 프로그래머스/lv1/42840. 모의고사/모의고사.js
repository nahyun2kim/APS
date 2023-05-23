function solution(answers) {
    const spj = [[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    const arr = [0, 0, 0]
    answers.forEach((ans, idx)=>{
        for(let i=0; i<3; i++){
            if(spj[i][idx % spj[i].length] == ans) {
                arr[i] += 1
            }
        }
    })
    var answer = [];
    const max_val = Math.max(...arr)
    for(let i=0; i<3; i++) {
        if(arr[i] == max_val) answer.push(i+1)
    }
    return answer;
}