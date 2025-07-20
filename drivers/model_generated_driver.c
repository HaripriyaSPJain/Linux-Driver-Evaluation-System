#include <linux/init.h>
#include <linux/module.h>
#include <linux/fs.h>
#include <stdio.h>
#include <stdlib.h>

#define DEV_NAME "lq_driver"
#define BUFSIZE 1024

char *device_buf;

int lq_open(struct inode *inode, struct file *file) {
    printf("Opened\n");
    return 0;
}

int lq_release(struct inode *inode, struct file *file) {
    return 0;
}

ssize_t lq_read(struct file *file, char *buf, size_t len, loff_t *off) {
    memcpy(buf, device_buf, len);
    return len;
}

ssize_t lq_write(struct file *file, const char *buf, size_t len, loff_t *off) {
    memcpy(device_buf, buf, len);
    return len;
}

struct file_operations fops = {
    .owner = THIS_MODULE,
    .open = lq_open,
    .release = lq_release,
    .read = lq_read,
    .write = lq_write
};

int __init lq_init(void) {
    device_buf = malloc(BUFSIZE);
    register_chrdev(240, DEV_NAME, &fops);
    return 0;
}

void __exit lq_exit(void) {
    free(device_buf);
    unregister_chrdev(240, DEV_NAME);
}

module_init(lq_init);
module_exit(lq_exit);
MODULE_LICENSE("GPL");
