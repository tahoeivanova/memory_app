% rebase('layout.tpl', title='Mnemotechnics')


<!-- Begin page content -->
<main role="main" class="flex-shrink-0">
  <div class="container">
  

<div id="carouselExampleInterval" class="carousel slide" data-ride="carousel">
  <div class="carousel-inner">

    <div class="carousel-item active" data-interval="1000">
      <div style="background-color: black; height: 300px;" class="d-block w-100"></div>
          <div class="carousel-caption d-none d-sm-block">
          <h1 style='margin-top: -150px; font-size: 72px;'>Старт!</h1>
        </div>
    </div>
% count = 0
% for number in random_numbers_global:
% count+=1

    <div class="carousel-item" data-interval="{{number_time}}" >
      <div style="background-color: black; height: 300px;" class="d-block w-100"></div>

        <div class="carousel-caption d-none d-sm-block">
          <h1 style='margin-top: -150px; font-size: 72px;'>{{number}}</h1>
          <p style='margin-top: -190px; color:grey;'>{{count}}/{{numbers_all}}</p>
        </div>

    </div>

        % end
    <div class="carousel-item" data-interval="10000" >

      <div style="background-color: black; height: 300px;" class="d-block w-100"></div>

        <div class="carousel-caption d-none d-sm-block">
          <h1 style='margin-top: -150px; font-size: 72px;'>Финиш!</h1>
        </div>

    </div>
  </div>
  <a class="carousel-control-prev" href="#carouselExampleInterval" role="button" data-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="sr-only">Previous</span>
  </a>
  <a class="carousel-control-next" href="#carouselExampleInterval" role="button" data-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="sr-only">Next</span>
  </a>
</div>
</div>


<br>
<div style="text-align: center;">
<form action="/number_input" method="POST">
    <input type="submit" value="Готово!">
</form>  
</div>


  </div>
</main>


