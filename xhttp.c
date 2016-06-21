#include <stdio.h>
#include <curl/curl.h>
#include <stdlib.h>
#include <string.h>
#include <openssl/md5.h>
#include <python2.7/Python.h>

size_t memory_callback(void *data, size_t size, size_t nmemb, void *content)
{
	size_t realsize = size *nmemb;
	char *p = *(char **)content;
	size_t len = p ? strlen(p) : 0;
	*(char **)content = realloc(p, len + realsize + 1);
	p = *(char **)content;
	memcpy(p + len, data, realsize);
	p[len + realsize] = '\0';
	
	return realsize;
}

size_t get_content(char *appid, char *secret_key, char *q, char *from ,char *to, char **content)
{
  CURL *curl;
  CURLcode res;
 
  curl = curl_easy_init();
  if(curl)
  {
	char myurl[1000] = "http://api.fanyi.baidu.com/api/trans/vip/translate?";
	char salt[60];
	int a = rand();
	sprintf(salt,"%d",a);
	char sign[120] = "";
	strcat(sign,appid);
	strcat(sign,q);
	strcat(sign,salt);
	strcat(sign,secret_key);
	//printf("%s\n",sign);
	unsigned char md[16];
	int i;
	char tmp[3]={'\0'},buf[33]={'\0'};

	MD5((const unsigned char *)sign, strlen((const char *)sign), md);

	for (i = 0; i < 16; i++)
	{
		sprintf(tmp,"%2.2x",md[i]);
		strcat(buf,tmp);
	}
	//printf("%s\n",buf);
	strcat(myurl,"appid=");
	strcat(myurl,appid);
	strcat(myurl,"&q=");
	strcat(myurl,q);
	strcat(myurl,"&from=");
	strcat(myurl,from);
	strcat(myurl,"&to=");
	strcat(myurl,to);
	strcat(myurl,"&salt=");
	strcat(myurl,salt);
	strcat(myurl,"&sign=");
	strcat(myurl,buf);
	printf("%s\n",myurl);

	/* always cleanup */
	curl_easy_setopt(curl, CURLOPT_URL, myurl);
	curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, memory_callback);
	curl_easy_setopt(curl, CURLOPT_WRITEDATA, (void *)content);
	
	res = curl_easy_perform(curl);
	/* Check for errors */ 
	if(res != CURLE_OK)
	  fprintf(stderr, "curl_easy_perform() failed: %s\n",
			  curl_easy_strerror(res));
	curl_easy_cleanup(curl);
	}
	return 0;
}

static PyObject *xhttp(PyObject *self, PyObject *args)
{
	char *content = NULL;
	char *appid;
	char *secret_key;
	char *q;
	char *from;
	char *to;
	if(!PyArg_ParseTuple(args, "s|ssss", &appid, &secret_key, &q, &from, &to))
	{
		return NULL;
	}
	get_content(appid, secret_key, q, from, to, &content);
	
	return Py_BuildValue("s", content);
	if(content) free(content);
}

static PyMethodDef httpMethods[] =
{
	{"xhttp", (PyCFunction)xhttp, METH_VARARGS},
	{NULL, NULL, 0, NULL}
};

PyMODINIT_FUNC initxhttp(void)
{
	Py_InitModule("xhttp", httpMethods);
}
