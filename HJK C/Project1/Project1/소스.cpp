#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{


	int a = 1;
	int b = 5;
	int add = a + b;
	printf("'a'는 %d이고, 'b'는 %d일때 a+b = %d", a, b, add);
	// [유인물 2번 문제]
		
	int kor;
	int eng;
	int mat;
	

	printf("국어, 영어,  수학 점수를 순서대로 입력하세요 >> ");
	scanf("%d %d %d", &kor, eng, mat);

	printf("국어 점수 %d\n영어 점수 %d\n수학 점수 %d", kor, eng, mat);

	//총점 계산
	int sum = kor + eng + mat;
	// 평균 계산
	float avg = sum / 3.0;

	return 0;
}