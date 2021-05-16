#include <Windows.h>
#include <iostream>
#include <vector>
#include <TlHelp32.h>
#include <Psapi.h>

#include "strobf.h"
#include "ntinfo.h"

std::vector<DWORD> threadList(DWORD pid) {
	/* solution from http://stackoverflow.com/questions/1206878/enumerating-threads-in-windows */
	std::vector<DWORD> vect = std::vector<DWORD>();
	HANDLE h = CreateToolhelp32Snapshot(TH32CS_SNAPTHREAD, 0);
	if (h == INVALID_HANDLE_VALUE)
		return vect;

	THREADENTRY32 te;
	te.dwSize = sizeof(te);
	if (Thread32First(h, &te)) {
		do {
			if (te.dwSize >= FIELD_OFFSET(THREADENTRY32, th32OwnerProcessID) +
				sizeof(te.th32OwnerProcessID)) {


				if (te.th32OwnerProcessID == pid) {
					//printf("PID: %04d Thread ID: 0x%04x\n", te.th32OwnerProcessID, te.th32ThreadID);
					vect.push_back(te.th32ThreadID);
				}

			}
			te.dwSize = sizeof(te);
		} while (Thread32Next(h, &te));
	}

	return vect;
}

DWORD GetThreadStartAddress(HANDLE processHandle, HANDLE hThread) {
	/* rewritten from https://github.com/cheat-engine/cheat-engine/blob/master/Cheat%20Engine/CEFuncProc.pas#L3080 */
	DWORD used = 0, ret = 0;
	DWORD stacktop = 0, result = 0;

	MODULEINFO mi;

	GetModuleInformation(processHandle, GetModuleHandle("kernel32.dll"), &mi, sizeof(mi));
	stacktop = (DWORD)GetThreadStackTopAddress_x86(processHandle, hThread);

	CloseHandle(hThread);

	if (stacktop) {
		//find the stack entry pointing to the function that calls "ExitXXXXXThread"
		//Fun thing to note: It's the first entry that points to a address in kernel32

		DWORD* buf32 = new DWORD[4096];

		if (ReadProcessMemory(processHandle, (LPCVOID)(stacktop - 4096), buf32, 4096, NULL)) {
			for (int i = 4096 / 4 - 1; i >= 0; --i) {
				if (buf32[i] >= (DWORD)mi.lpBaseOfDll && buf32[i] <= (DWORD)mi.lpBaseOfDll + mi.SizeOfImage) {
					result = stacktop - 4096 + i * 4;
					break;
				}

			}
		}

		delete buf32;
	}

	return result;
}

DWORD GetThreadstackStartAddress(int stackNumber, DWORD pID, HANDLE processHandle) {
	std::vector<DWORD> threadId = threadList(pID);
	int stackNum = 0;
	for (auto it = threadId.begin(); it != threadId.end(); ++it) {
		HANDLE threadHandle = OpenThread(THREAD_GET_CONTEXT | THREAD_QUERY_INFORMATION, FALSE, *it);
		DWORD threadStartAddress = GetThreadStartAddress(processHandle, threadHandle);
		//printf("TID: 0x%04x = THREADSTACK%2d BASE ADDRESS: 0x%04x\n", *it, stackNum, threadStartAddress);
		if (stackNum == stackNumber) return threadStartAddress;
		stackNum++;
	}
	return 0;
}

HANDLE getProcHdlByName(LPCSTR process)
{
	PROCESSENTRY32 entry;
	entry.dwSize = sizeof(PROCESSENTRY32);

	HANDLE snapshot = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, NULL);

	if (Process32First(snapshot, &entry) == TRUE)
	{
		while (Process32Next(snapshot, &entry) == TRUE)
		{
			if (strcmp(entry.szExeFile, process) == 0)
			{
				HANDLE hProcess = OpenProcess(PROCESS_ALL_ACCESS, FALSE, entry.th32ProcessID);
				return hProcess;
			}
		}
	}

	CloseHandle(snapshot);

	return NULL;
}

DWORD getProcIdByName(LPCSTR process)
{
	PROCESSENTRY32 entry;
	entry.dwSize = sizeof(PROCESSENTRY32);

	HANDLE snapshot = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, NULL);

	if (Process32First(snapshot, &entry) == TRUE)
	{
		while (Process32Next(snapshot, &entry) == TRUE)
		{
			if (strcmp(entry.szExeFile, process) == 0)
			{
				return entry.th32ProcessID;
			}
		}
	}

	CloseHandle(snapshot);

	return 0;
}

DWORD ReadPtr(HANDLE hProcess, void* addr, std::vector<DWORD> offsets)
{
	DWORD ptr_val;

	if (ReadProcessMemory(hProcess, addr, &ptr_val, sizeof(ptr_val), NULL) != 0)
	{
		for (uint32_t i = 0; i < offsets.size(); i++)
			ptr_val = ReadPtr(hProcess, (void*)(ptr_val + offsets[i]), {});
		return ptr_val;
	}
}

bool check_score(char *score)
{
	if (strlen(score) < 7)
		return false;
	if (score[1] != '0')
		return false;
	if (score[4] != '0')
		return false;
	if (1 == 99)
		return false;
	if (score[6] != '0')
		return false;
	if (score[0] != '1')
		return false;
	if (score[2] != '0')
		return false;
	if ('a' == 'z')
		return false;
	if (score[5] != '0')
		return false;
	if (score[3] != '0')
		return false;
	return true;
}

INT WINAPI WinMain(__in HINSTANCE hInstance, __in_opt HINSTANCE hPrevInstance, __in PSTR pCmdLine, __in INT nCmdShow)
{
	char buff[8] = { 0 };
	HANDLE hProcess = NULL;
	DWORD pID = 0;
	DWORD PointerBaseAddress = 0;
	DWORD offsetGameToBaseAdress = -0x00000980;
	std::vector<DWORD> pointsOffsets{ 0x848, 0x20, 0x0, 0x8, 0x90 };

	while (true)
	{
		hProcess = getProcHdlByName("Red Aleph.exe");
		pID = getProcIdByName("Red Aleph.exe");
		PointerBaseAddress = GetThreadstackStartAddress(0, pID, hProcess);
		DWORD ptrval = ReadPtr(hProcess, (void*)(PointerBaseAddress + offsetGameToBaseAdress), pointsOffsets);

		std::cout << ptrval << std::endl;
		sprintf_s(buff, 8, "%d", ptrval);
		if (buff && check_score(buff) == true) {
			MessageBoxA(nullptr, OBFUSCATE("CYBERTF{Y0u_H4ck3d_Th3_G4m3}"), OBFUSCATE("Info"), MB_OK | MB_ICONINFORMATION);
		}
		Sleep(2000);
	}
}