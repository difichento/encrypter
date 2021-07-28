
<h1 id="-2999">ШИФРАТОР</h1>
<blockquote>
<p>ШИФРАТОР - программа на python для шифрования текста несколькими способами, которые будут описаны ниже.</p>
</blockquote>
<h1 id="-">Гайд по запуску</h1>
<h3 id="-python-"><strong>Первый этап: установка python и нужные библиотеки</strong></h3>
<h5 id="-python3-pygame-">Если у вас уже установлен python3 — пропустите этот этап</h5>
<p><strong>1. Скачайте python3 с официального <a href="https://www.python.org/downloads/">сайта</a> и установите его.</strong> 
<strong>2. Во время установки <em>обязательно</em> поставьте галочку "Add Python 3.x to PATH".</strong></p> <p><img src="https://python-scripts.com/wp-content/uploads/2018/06/win-install-dialog.40e3ded144b0.png" alt="add path screenshot"></p>
<p><strong>3. Запустите консоль Windows любым удобным для вас способом (например набрав в поиске приложений cmd)</strong></p>
<p><strong>4. Установите нужные библиотеки используя команды</strong></p>
<blockquote>
<p>pip install Pillow</p>
</blockquote>
<h3 id="-"><strong>Второй этап: запуск программы</strong></h3>
<p><strong>1. Скачайте проект с github любым удобным для вас способом (gitclone или по <a href="">ссылке</a>.</strong></p>
<p><strong>2. В консоли перейдите в папку с игрой при помощи команды cd.</strong></p>
<p><strong>3. Запустите игру при помощи команды</strong></p>
<blockquote>
<p>python main.py</p>
</blockquote>
<p>для запуска в консоли, или</p>
<blockquote>
<p>python main_graph.py</p>
</blockquote>
<p>для запуска гарфического интерфейса</p>
<p><strong>4. Зашифруйте весь текст на своем компьютере</strong></p>
<h1 id="-"><strong>Интерфейс программы и доступные виды шифрования</strong></h1>
<p>В программе доступно 4 вида шифрования:</p>
<ul>
<li><details><summary>Шифр Цезаря</summary>
Как работает: <a href="https://ru.wikipedia.org/wiki/%D0%A8%D0%B8%D1%84%D1%80_%D0%A6%D0%B5%D0%B7%D0%B0%D1%80%D1%8F">ссылка</a>
  <p>На вход подается файл с текстом, файл куда будет сохранен результат, и сдвиг</p>
  <p>Также есть возможность расшифровать текст методом частотного анализа</p>
<p><img src="https://d.radikal.ru/d30/2104/dd/0ca0a841488c.png" alt="скрин"></li></p>
  </details>
<li><details><summary>Шифр Виженера</summary>
Как работает: <a href="https://ru.wikipedia.org/wiki/%D0%A8%D0%B8%D1%84%D1%80_%D0%92%D0%B8%D0%B6%D0%B5%D0%BD%D0%B5%D1%80%D0%B0">ссылка</a>
  
<p>На вход подается файл с текстом, файл, куда будет сохранен результат и ключевое слово</p>
<p><img src="https://d.radikal.ru/d25/2104/20/22ccacdaccf2.png" alt="скрин"></p></li>
  </details>
<li><details><summary>Шифр Вернама</summary>
Работает почти как шифр Виженера, но генерирует случайный ключ (из сида) такой же по длинне как и шифруемый текст
  <p><img src="https://c.radikal.ru/c02/2104/2c/e60918e1d4ed.png" alt="скрин"></p></li>
</details>
<p><li><details><summary>Шифрование в картинку</summary></p>
<p>Зашифровывает текст в случайные пиксели картинки так, что это практически незаметно для человеческого глаза.</p>
  <p>Для шифровки и расшифровки понадобится один и тот же сид</p>
  <p><img src="https://a.radikal.ru/a29/2104/ea/bca59593cdd4.png" alt="скрин"></p></li>
</details>
</ul>
<h2 id="-">Несколько примеров работы шифратора</h2>
<p><strong>Шифр вернама</strong></p>
<p><img src="https://b.radikal.ru/b40/2104/04/476c2d9bac82.png" alt=""></p>
<p><strong>Шифрование в картинку</strong></p>
<p><img src="https://d.radikal.ru/d00/2104/63/099a405c47aa.png" alt=""></p>
<p><img src="https://a.radikal.ru/a07/2104/d0/8d66912e2de5.png" alt=""></p>
<p><img src="https://d.radikal.ru/d43/2104/a2/a74f4656723f.png" alt=""></p>
