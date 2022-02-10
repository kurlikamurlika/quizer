function byTime() {

document.getElementById("quiz_list").innerHTML = `<table class="table">
        <thead>
        <tr>
            <th>Sort By:</th>
            <th><a href="#" onclick="byLength()" style="text-decoration: none" class="btn btn-secondary">№ of questions</a></th>
            <th><a href="#" onclick="byPlays()" style="text-decoration: none" class="btn btn-secondary">№ of plays</a></th>
            <th><a href="#" onclick="byTime()" style="text-decoration: none" class="btn btn-secondary">Publication date</a></th>
        </tr>
        </thead>
        <tbody>
            {% for quiz in quiz_time_descending %}
                <tr class="{% cycle 'bg-warning' 'bg-info' %}">
                    <td>
                        <a href="{% url 'quiz:play' quiz.0.id%}" style="text-decoration: none"><h3 class="text-danger card-title">{{ forloop.counter }}. {{ quiz.0.quiz_name }}</h3></a>
                        <a href="{% url 'quiz:profile' quiz.0.user.id%}" style="text-decoration: none"><h5>{{ quiz.0.user.username }}</h5></a>
                    </td>
                    <td><h3 class="mx-5">{{ quiz.3 }}</h3></td>
                    <td><h3 class="mx-5">{{ quiz.2 }}</h3></td>
                    <td><h3 class="mx-5">{{ quiz.1 }}</h3></td>
                </tr>
            {% endfor %}
        </tbody>
        </table>`;
}

function byLength() {
document.getElementById("quiz_list").innerHTML = `<table class="table">
        <thead>
        <tr>
            <th>Sort By:</th>
            <th><a href="#" onclick="byLength()" style="text-decoration: none" class="btn btn-secondary">№ of questions</a></th>
            <th><a href="#" onclick="byPlays()" style="text-decoration: none" class="btn btn-secondary">№ of plays</a></th>
            <th><a href="#" onclick="byTime()" style="text-decoration: none" class="btn btn-secondary">Publication date</a></th>
        </tr>
        </thead>
        <tbody>
            {% for quiz in quiz_length_descending %}
                <tr class="{% cycle 'bg-warning' 'bg-info' %}">
                    <td>
                        <a href="{% url 'quiz:play' quiz.0.id%}" style="text-decoration: none"><h3 class="text-danger card-title">{{ forloop.counter }}. {{ quiz.0.quiz_name }}</h3></a>
                        <a href="{% url 'quiz:profile' quiz.0.user.id%}" style="text-decoration: none"><h5>{{ quiz.0.user.username }}</h5></a>
                    </td>
                    <td><h3 class="mx-5">{{ quiz.3 }}</h3></td>
                    <td><h3 class="mx-5">{{ quiz.2 }}</h3></td>
                    <td><h3 class="mx-5">{{ quiz.1 }}</h3></td>
                </tr>
            {% endfor %}
        </tbody>
        </table>`;
}

function byPlays() {
document.getElementById("quiz_list").innerHTML = `<table class="table">
        <thead>
        <tr>
            <th>Sort By:</th>
            <th><a href="#" onclick="byLength()" style="text-decoration: none" class="btn btn-secondary">№ of questions</a></th>
            <th><a href="#" onclick="byPlays()" style="text-decoration: none" class="btn btn-secondary">№ of plays</a></th>
            <th><a href="#" onclick="byTime()" style="text-decoration: none" class="btn btn-secondary">Publication date</a></th>
        </tr>
        </thead>
        <tbody>
            {% for quiz in quiz_plays_descending %}
                <tr class="{% cycle 'bg-warning' 'bg-info' %}">
                    <td>
                        <a href="{% url 'quiz:play' quiz.0.id%}" style="text-decoration: none"><h3 class="text-danger card-title">{{ forloop.counter }}. {{ quiz.0.quiz_name }}</h3></a>
                        <a href="{% url 'quiz:profile' quiz.0.user.id%}" style="text-decoration: none"><h5>{{ quiz.0.user.username }}</h5></a>
                    </td>
                    <td><h3 class="mx-5">{{ quiz.3 }}</h3></td>
                    <td><h3 class="mx-5">{{ quiz.2 }}</h3></td>
                    <td><h3 class="mx-5">{{ quiz.1 }}</h3></td>
                </tr>
            {% endfor %}
        </tbody>
        </table>`;

}