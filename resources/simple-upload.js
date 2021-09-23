import Uploader from "simple-uploader.js";
import {v4} from "uuid";
import axios from "axios";

export function uploaderFactory(url, onMerged, onProgress) {
    const uploader = new Uploader({
        target: url,
        headers: {},
        singleFile: true,
        simultaneousUploads: 3,
        chunkSize: 10 * 1024 * 1024,
        successStatuses: [200, 201, 202],
        permanentErrors: [400, 415, 500, 501],
        testChunks: false,
        maxChunkRetries: 0,
        chunkRetryInterval: null,
        progressCallbacksInterval: 500,
        allowDuplicateUploads: false,
        generateUniqueIdentifier: () => v4()
    });

    uploader.on("fileProgress", function (rootFile, file, chunk) {
        onProgress && onProgress(file.progress())
    });

    uploader.on("fileSuccess", function (rootFile, file, message, chunk) {
        const mergeData = {
            identifier: rootFile.uniqueIdentifier,
            filename: rootFile.name,
            chunk_size: rootFile.chunks.length
        };
        axios.put(url, mergeData).then(({data}) => {
            onMerged && onMerged(data, mergeData);
        });
    });

    return uploader;
}
