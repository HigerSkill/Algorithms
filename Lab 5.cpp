#include<stdio.h>
#include<mpi.h>
#define n 16

int main(int argc, char* argv[]) {
	unsigned long long A[n], prod_total, prod_on_process = 1;
	int rank, size;
	double time_begin, time_end, time_diff;
	int num_amount, left_border, right_border;

	MPI_Status status;
	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &rank);
	MPI_Comm_size(MPI_COMM_WORLD, &size);

	for (int i = 0; i < n; ++i) {
		A[i] = i+1;
	}

	MPI_Bcast(A, n, MPI_INT, 0, MPI_COMM_WORLD);
	
	num_amount = n / size;
	left_border = num_amount * rank;
	if (rank == size - 1) {
		right_border = n;
	}
	else {
		right_border = left_border + num_amount;
	}
	for (int i = left_border; i < right_border; ++i) {
		prod_on_process = prod_on_process * A[i];
	}

	time_begin = MPI_Wtime();
	for (int k = 0; k < 100; ++k) {
		MPI_Reduce(&prod_on_process, &prod_total, 1, MPI_UNSIGNED_LONG_LONG, MPI_PROD, 0, MPI_COMM_WORLD);
	}
	time_end = MPI_Wtime();
	time_diff = time_end - time_begin;
	printf("\nrank=%d model time=%lf\n", rank, time_diff);

	if (rank == 0) {
		printf("\n Total product = %llu", prod_total);
	}
	MPI_Finalize();
}
