% rebase('layout.tpl', title="Mnemotechnics")


<!-- Begin page content -->
<main role="main" class="flex-shrink-0">
  <div class="container" style="margin-top: 100px">




<div id="carouselExampleInterval" class="carousel slide" data-ride="carousel">
  <div class="carousel-inner">

    <div class="carousel-item active" data-interval="5000">
      <div style="background-color: black; height: 300px;" class="d-block w-100"></div>
          <div class="carousel-caption d-none d-sm-block">
          <h1 style='margin-top: -150px; font-size: 72px;'>Старт!</h1>
        </div>
    </div>

% for card in cards_shuffled:


 <div class="carousel-item" data-interval="{{cards_time}}" style="text-align: center">
        <img src="static/img/{{card}}.png" style="height: 300px;"  alt="{{card}}">

        <div class="carousel-caption d-none d-md-block">

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

<br>
<div style="text-align: center;">
<form action="/cards_input" method="POST">
    <input type="submit" value="Готово!">
</form>  
</div>


  </div>
</main>


