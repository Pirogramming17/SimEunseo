from django.shortcuts import render
from .models import Review
from django.shortcuts import redirect

def review_list(request):
    order_list = ['작성시간순','개봉년도순','제목순','별점순']
    order = request.GET.get('order', None)
    if order == order_list[0]:
        reviews = Review.objects.all().order_by('-created_date')
    elif order == order_list[1]:
        reviews = Review.objects.all().order_by('-year')
    elif order == order_list[2]:
        reviews = Review.objects.all().order_by('-title')
    elif order == order_list[3]:
        reviews = Review.objects.all().order_by('-star')
    else :
        reviews = Review.objects.all()
        
    context = {
        "reviews": reviews,
        "order_list" : order_list,
        "order" : order,
    }
    return render(request, template_name='reviews/review_list.html', context=context) 

def review_create(request):
    genres = Review.GENRE_CHOICES
    
    if request.method == 'POST':
        # post 요청 값 받기 
        title = request.POST["title"]
        year = request.POST["year"]
        genre = request.POST["genre"]
        star = request.POST["star"]
        runtime = request.POST["runtime"]
        review = request.POST["review"]
        director = request.POST["director"]
        actor = request.POST["actor"]

        # 데이터 베이스에 저장하기 
        Review.objects.create(title=title, year=year, genre=genre, star=star, runtime=runtime, review=review, director=director, actor=actor)
        return redirect("/review")
        
    context = {"genres": genres}
    return render(request, template_name ="reviews/review_create.html", context=context)

def review_detail(request, id):
    review = Review.objects.get(id=id)
    runtime = f'{review.runtime//60}시간 {review.runtime%60}분'
    context = {
        "review" : review,
        "runtime" : runtime
    }
    return render(request, template_name="reviews/review_detail.html", context=context)

def review_update(request, id):
    genres = Review.GENRE_CHOICES
    if request.method == "POST":
        title = request.POST["title"]
        year = request.POST["year"]
        genre = request.POST["genre"]
        star = request.POST["star"]
        runtime = request.POST["runtime"]
        review = request.POST["review"]
        director = request.POST["director"]
        actor = request.POST["actor"]
        
        Review.objects.filter(id=id).update(title=title, year=year, genre=genre, star=star, runtime=runtime, review=review, director=director, actor=actor)
        return redirect(f"/review/{id}")
    
    elif request.method == "GET":
        review = Review.objects.get(id=id)
        context = {
            "review" : review,
            "genres" : genres,
        }
        return render(request, template_name="reviews/review_update.html", context=context)
    
def review_delete(request, id):
    if request.method == "POST":
        review = Review.objects.get(id=id)
        review.delete()
    return redirect("/review")