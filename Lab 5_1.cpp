#include<stdio.h>
#include<iostream>
#include<mpi.h>
#define n 16

int main(int argc, char* argv[]) {
	unsigned long long A[n], mem_total, mem_val, total_val, rec_val = 1;
	int rank, size, num_process;
	double time_begin, time_end, time_diff;
	int num_amount, left_border, right_border;

	MPI_Status status;
	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &rank);
	MPI_Comm_size(MPI_COMM_WORLD, &size);
	num_process = size;
	
	for (int i = 0; i < n; ++i) {
		A[i] = i+1;
	}

	num_amount = n / size;
	left_border = num_amount * rank;
	if (rank == size - 1) {
		right_border = n;
	}
	else {
		right_border = left_border + num_amount;
	}
	for (int i = left_border; i < right_border; ++i) {
		rec_val = rec_val * A[i];
	}
	mem_total = mem_val = total_val = rec_val;
	
	time_begin = MPI_Wtime();
	
	for (int k = 0; k < 100; ++k) {
		total_val = rec_val = mem_total = mem_val;
		num_process = size;
		while (num_process > 1) {
			if (rank < num_process / 2) {
				MPI_Recv(&rec_val, 1, MPI_UNSIGNED_LONG_LONG, num_process - rank - 1, 1, MPI_COMM_WORLD, &status);
				total_val = rec_val * total_val;
			}
			else if (rank < num_process) {
				MPI_Send(&total_val, 1, MPI_UNSIGNED_LONG_LONG, num_process - rank - 1, 1, MPI_COMM_WORLD);
			}
			num_process = num_process / 2;
		}
	}
	
	time_end = MPI_Wtime();
	time_diff = time_end - time_begin;
	printf("\nrank = %d, time = %lf \n", rank, time_diff);

	if (rank == 0) {
		printf("Total = %llu \n", total_val);
	}
	MPI_Finalize();
}
