console.log('Its working');

let theme = localStorage.getItem('theme')

if (theme == null) {
    setTheme('light')
} else {
    setTheme(theme)
}

let themeDots = document.getElementsByClassName('theme-dot')

for (var i = 0; i < themeDots.length; i++) {
    themeDots[i].addEventListener('click', function () {
        let mode = this.dataset.mode;
        console.log('Option clicked:', mode)
        setTheme(mode);
    });
}
console.log('Its working')
function setTheme(mode) {
    if (mode == 'light') {
        document.getElementById('theme-style').href = staticPath + '/default.css'
    }

    if (mode == 'blue') {
        document.getElementById('theme-style').href = staticPath + '/blue.css'
    }

    if (mode == 'green') {
        document.getElementById('theme-style').href = staticPath + '/green.css'
    }

    if (mode == 'purple') {
        document.getElementById('theme-style').href = staticPath + '/purple.css'
    }

    localStorage.setItem('theme', mode)
}
