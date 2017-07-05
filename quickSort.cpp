template <typename T, size_t right>
void quickSort(T (&arr)[right], int left, int right)
{	
	int i = left;
	int j = right;
	T tmp;
	T pivot = arr[(left + right) / 2];
  
	while (i <= j)
	{
		while (arr[i] < pivot)
			i++;	
		while (arr[j] > pivot)
			j--;

		if (i <= j)
		{
			tmp = arr[i];
			arr[i] = arr[j];
			arr[j] = tmp;
			i++;
			j--;
		}
	}

	if (left < j) 
		quickSort(arr, left, j);
	if (i < right)
		quickSort(arr, i, right);
}
