function addQuestion() {
    let question_list = document.getElementsByClassName('question_text');
    for (let i of question_list){
        var question_number = i.innerHTML.slice(14);
    }

    document.getElementById("quiz_form").innerHTML += `
    <br>
    <label>Question text:</label>
    <input name="question_text" type="text" required>
    <a onclick="addAnswer()" class="btn btn-sm btn-secondary">Add answer</a>`;
}

function addAnswer() {
    document.getElementById('quiz_form').innerHTML +=
        `<div class="container">
            <label>Answer text:</label>
            <input type="text" name="answer_text" required>
            <label>Given points:</label>
            <input type="number" name="given_points" required>
         </div>`;
}

function Reset() {
    document.getElementById("quiz_form").innerHTML = `
        <label>Enter name of your quiz:</label>
        <input type="text" name="quiz_name" id="quiz_name" required><br><br>
        <label>Question text:</label>
        <input name="question_text_1" type="text" class="question_text" required>
        <a onClick="addAnswer()" class="btn btn-sm btn-secondary">Add answer</a>
`}