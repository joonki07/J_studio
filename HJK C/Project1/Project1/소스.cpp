#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{


	int a = 1;
	int b = 5;
	int add = a + b;
	printf("'a'�� %d�̰�, 'b'�� %d�϶� a+b = %d", a, b, add);
	// [���ι� 2�� ����]
		
	int kor;
	int eng;
	int mat;
	

	printf("����, ����,  ���� ������ ������� �Է��ϼ��� >> ");
	scanf("%d %d %d", &kor, eng, mat);

	printf("���� ���� %d\n���� ���� %d\n���� ���� %d", kor, eng, mat);

	//���� ���
	int sum = kor + eng + mat;
	// ��� ���
	float avg = sum / 3.0;

	return 0;
}