#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

/**
 * infinite_while - a function that runs an infinite while loop
 *
 * Return: Always return 0
*/

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - a function that creates five zombie processes.
 *
 * Return: Always return 0
*/

int main(void)
{
	pid_t zom_pid;
	char n_cont;

	for (n_cont = 0; n_cont < 5; n_cont++)
	{
		zom_pid = fork();
		if (zom_pid > 0)
		{
			printf("Zombie process created, PID: %d\n", zom_pid);
			sleep(1);
		}
		else
		{
			exit(0);
		}
	}
	infinite_while();

	return (EXIT_SUCCESS);
}
